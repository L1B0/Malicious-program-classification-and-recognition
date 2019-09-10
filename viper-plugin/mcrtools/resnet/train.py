from keras.models import save_model
from keras.utils import np_utils
from keras.callbacks import Callback
from keras import backend as K
from sklearn.metrics import f1_score, precision_score, recall_score
from gensim.models import word2vec

import os
import re
import numpy as np
import tensorflow as tf

from .ResNet import ResNetBuilder


class Metrics(Callback):
	def on_train_begin(self, logs={}):
		self.val_f1s = []
		self.val_recalls = []
		self.val_precisions = []

	def on_epoch_end(self, epoch, logs={}):
		#         val_predict = (np.asarray(self.model.predict(self.validation_data[0]))).round()
		val_predict = np.argmax(np.asarray(self.model.predict(self.validation_data[0])), axis=1)
		#         val_targ = self.validation_data[1]
		val_targ = np.argmax(self.validation_data[1], axis=1)
		_val_f1 = f1_score(val_targ, val_predict, average='micro')
		_val_recall = recall_score(val_targ, val_predict, average='micro')
		_val_precision = precision_score(val_targ, val_predict, average='micro')
		self.val_f1s.append(_val_f1)
		self.val_recalls.append(_val_recall)
		self.val_precisions.append(_val_precision)
		print('\n— val_f1: %f — val_precision: %f — val_recall %f' % (_val_f1, _val_precision, _val_recall))
		# print(' — val_f1:' ,_val_f1)
		return


def set_config():
	config = tf.ConfigProto(allow_soft_placement=True, device_count={'GPU': 1})
	session = tf.Session(config=config)
	K.set_session(session)


def load_training_data(path, top100_path):
	"""
	Load training data from files
	:param path: the path of training dataset
	:param top100_path: the path of top100.txt
	:return: samples and labels
	"""
	X_train = []
	y_train = []

	with open(top100_path, 'r') as f:
		top100 = f.read()
		pattern = re.compile(r'[\"\'](.*?)[\"\']')
		top100_result = pattern.findall(top100)[:100]

	# Load training data
	dirs = os.listdir(path)
	cnt = 0
	for dir in dirs:
		files = os.listdir(path + dir)
		for file in files:
			# Load word2vec model
			word_model = word2vec.Word2Vec.load(path + dir + "/" + file)

			# Convert files into matrices using top100.txt
			matrix = np.zeros((100, 100))
			for i in range(100):
				try:
					matrix[i] = word_model[top100_result[i]]
				except:
					matrix[i] = np.zeros(100)
			matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min()) * 255
			matrix = matrix.astype(np.uint8)
			# if cnt < 4:
			# 	cv2.imwrite("./train_image/" + dir + str(cnt) + '.jpg', matrix)
			# 	cnt += 1
			X_train.append(np.reshape(matrix, (100, 100, 1)))
			y_train.append(cnt)
		cnt += 1

	return np.array(X_train), np.array(y_train)


def load_test_data(path, top100_path):
	"""
	Load test data from files
	:param path: the path of test dataset
	:param top100_path: the path of top100.txt
	:return: samples, labels and names of all samples
	"""
	X_test = []
	y_test = []
	file_names = []
	category_names = []

	with open(top100_path, 'r') as f:
		top100 = f.read()
		pattern = re.compile(r'\"(.*?)\"')
		top100_result = pattern.findall(top100)

	# Load test data
	dirs = os.listdir(path)
	cnt = 0
	for dir in dirs:
		output_image = 0
		category_names.append(dir)
		files = os.listdir(path + dir)
		for file in files:
			# Vectorize .ans file
			word_model = word2vec.Word2Vec.load(path + dir + "/" + file)

			# Convert files into matrices using top100.txt
			matrix = np.zeros((100, 100))
			for i in range(100):
				try:
					matrix[i] = word_model[top100_result[i]]
				except:
					matrix[i] = np.zeros(100)

			matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min()) * 255
			matrix = matrix.astype(np.uint8)
			# if not os.path.exists('test_image'):
			# 	os.mkdir('test_image')
			# if output_image < 4:
			# 	cv2.imwrite("./test_image/" + dir + str(output_image) + '.jpg', matrix)
			# 	time.sleep(3)
			# 	output_image += 1
			X_test.append(np.reshape(matrix, (100, 100, 1)))
			y_test.append(cnt)
			file_names.append(file.strip('.asm.ans.model'))
		cnt += 1

	return np.array(X_test), np.array(y_test), file_names, category_names


def train_resnet(training_path, test_path, top_100_path, model_path):
	"""
	Train ResNet model and save it
	:param training_path: the path of training dataset
	:param test_path: the path of test dataset
	:param top_100_path: the path of top100.txt
	:param model_path: the path of ResNet model
	"""
	set_config()

	# Hyperparameters
	batch_size = 64
	class_number = 6
	epoch = 20

	img_rows, img_cols = 100, 100
	img_channels = 1

	X_train, y_train = load_training_data(training_path, top_100_path)
	X_test, y_test, file_names, category_names = load_test_data(test_path, top_100_path)

	X_train = X_train.astype('float32')
	X_test = X_test.astype('float32')

	y_train = np_utils.to_categorical(y_train, class_number)
	y_test = np_utils.to_categorical(y_test, class_number)

	model = ResNetBuilder.build_resnet_18((img_channels, img_rows, img_cols), class_number)

	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	# metrics = Metrics()
	# model.fit(X_train, y_train, epochs=epoch, batch_size=batch_size, validation_data=(X_test, y_test),
	#           callbacks=[metrics])
	model.fit(X_train, y_train, epochs=epoch, batch_size=batch_size)

	accuracy = model.evaluate(X_test, y_test, batch_size=batch_size)
	print(accuracy)

	if not os.path.exists(model_path):
		os.mkdir(model_path)
	save_model(model, model_path + 'ResNet_model.h5')

	return accuracy


if __name__ == "__main__":
	train_resnet("../train/", "../test/", "../model/")
