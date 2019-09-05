from keras.models import Model
from keras.layers import Input, Activation, Dense, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D, AveragePooling2D
from keras.layers.merge import add
from keras.layers.normalization import BatchNormalization
from keras import backend as K


def bn_relu(input):
	"""
	The batch normalization and activation layer using 'relu'.
	:param input: The input tensor.
	:return: Normalized and activated output.
	"""
	norm = BatchNormalization(axis=3)(input)

	return Activation("relu")(norm)


def bn_relu_conv(filters, kernel_size, strides):
	"""
	The block using in residual block.
	:param filters: The dimensionality of the output space.
	:param kernel_size: The kernel size in the convolution layer.
	:param strides: The strides in the convolution layer.
	:return: The output of block unit.
	"""

	def f(input):
		activation = bn_relu(input)

		return Conv2D(filters=filters, kernel_size=kernel_size, strides=strides, padding="same")(activation)

	return f


def shortcut(input, residual):
	"""
	The shortcut between input and residual block.
	:param input: The input tensor.
	:param residual: The residual block output tensor.
	:return: The merged filter.
	"""

	# Calculate the convolution stride to make sure that the dimensionality of the input and the residual are the same
	input_shape = K.int_shape(input)
	residual_shape = K.int_shape(residual)
	stride_width = int(round(input_shape[1] / residual_shape[1]))
	stride_height = int(round(input_shape[2] / residual_shape[2]))
	equal_channels = input_shape[3] == residual_shape[3]

	shortcut = input

	# Width or height or channels is not equal, using 1*1 convolution to make them equal.
	if stride_width > 1 or stride_height > 1 or not equal_channels:
		shortcut = Conv2D(filters=residual_shape[3], kernel_size=1, strides=(stride_width, stride_height),
		                  padding="valid")(input)

	return add([shortcut, residual])


def residual_block(block_function, filters, repetitions, is_first_layer):
	"""
	Build a residual block with repeating bottleneck blocks.
	:param block_function: The block function to use. This is either "basic_block" or "bottleneck_block".
	:param filters: The dimensionality of the output space.
	:param repetitions: How many times residual block unit repeats.
	:param is_first_layer: Check if this block is the first layer of the whole network (that is the first convolution layer).
	:return: The output of residual block.
	"""

	def f(input):
		for i in range(repetitions):
			strides = 1
			if i == 0 and not is_first_layer:
				strides = 2
			input = block_function(filters=filters, strides=strides,
			                       is_first_block_of_first_layer=(is_first_layer and i == 0))(input)

		return input

	return f


def basic_block(filters, strides, is_first_block_of_first_layer):
	"""
	Without using bottleneck.
	:param filters: The dimensionality of the output space.
	:param strides: The strides in the convolution layer.
	:param is_first_block_of_first_layer: Check if this layer is the first block of the first layer.
	:return: The output of a basic block.
	"""

	def f(input):
		# Check if batch normalization and activation is required
		if is_first_block_of_first_layer:
			# Batch normalization and relu have been done before building blocks
			conv = Conv2D(filters=filters, kernel_size=3, strides=strides, padding="same")(input)
		else:
			conv = bn_relu_conv(filters=filters, kernel_size=3, strides=strides)(input)

		residual = bn_relu_conv(filters=filters, kernel_size=3, strides=1)(conv)

		return shortcut(input, residual)

	return f


class ResNetBuilder(object):
	@staticmethod
	def build(input_shape, num_output, block_function, repetitions):
		# Because backend is tensorflow, channels are in the third dimension
		input_shape = (input_shape[1], input_shape[2], input_shape[0])
		input = Input(shape=input_shape)

		conv1 = bn_relu(Conv2D(filters=64, kernel_size=7, strides=2, padding="same")(input))
		pool1 = MaxPooling2D(pool_size=3, strides=2, padding="same")(conv1)

		block = pool1
		filters = 64

		for i, r in enumerate(repetitions):
			block = residual_block(block_function, filters=filters, repetitions=r, is_first_layer=(i == 0))(block)
			filters *= 2

		block = bn_relu(block)

		block_shape = K.int_shape(block)

		pool2 = AveragePooling2D(pool_size=(block_shape[1], block_shape[2]), strides=1)(block)
		flatten = Flatten()(pool2)
		dense = Dense(units=num_output, activation="softmax")(flatten)
		model = Model(inputs=input, outputs=dense)

		return model

	@staticmethod
	def build_resnet_18(input_shape, num_outputs):
		return ResNetBuilder.build(input_shape, num_outputs, basic_block, [2, 2, 2, 2])
