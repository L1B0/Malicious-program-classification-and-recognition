from preprocessing.word2vec import batch_vectorize_asm
from preprocessing.generate_dataset import generate_dataset
from resnet.train import train_resnet
from tf_idf import train_dnn
from predict import classify_program


def train(ans_path, func_path):
	"""
	Train models using ResNet and DNN and merge them
	:param ans_path: the path of .asm.ans files
	:param func_path: the path of .vec files
	:return: Merged model
	"""
	work_path = '/'.join(ans_path.split('/')[0:-3]) + '/'
	model_path = work_path + 'model/'

	'''--------ResNet Model--------'''
	# Vectorize the .asm.ans files and save them to word2vec_model_path
	word2vec_model_path = work_path + 'word2vec_train/'
	batch_vectorize_asm(ans_path, word2vec_model_path)

	# Generate the dataset from .asm.ans.model files and split them into training dataset and test dataset
	resnet_training_path = work_path + 'resnet_train/'
	resnet_test_path = work_path + 'resnet_test/'
	top_100_path = '/'.join(ans_path.split('/')[0:-2]) + '/top100.txt'
	generate_dataset(word2vec_model_path, resnet_training_path, resnet_test_path)

	# Train ResNet model
	train_resnet(resnet_training_path, resnet_test_path, top_100_path, model_path)

	'''--------DNN Model--------'''
	# Generate the dataset from .vec files and split them into training dataset and test dataset
	dnn_training_path = work_path + 'func_train/'
	dnn_test_path = work_path + 'func_test/'
	generate_dataset(func_path, dnn_training_path, dnn_test_path)

	# Train DNN model
	train_dnn(dnn_training_path, dnn_test_path, model_path)


def predict(ans_path, func_path):
	"""
	Predict the macilious programs and save predictions as a .txt file
	:param ans_path: the path of .asm.ans files
	:param func_path: the path of .vec files
	"""
	classify_program(ans_path, func_path, "./model/")


if __name__ == "__main__":
	train('./data/ans/', './data/functimes/')
	predict('./resnet_test/', './func_test/')
