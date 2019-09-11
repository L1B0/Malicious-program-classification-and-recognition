from keras.models import load_model

import numpy as np
import os
import re

from .resnet import train
from .tf_idf import load_data
from .preprocessing.word2vec import my_word2vec


def classify_program(ans_path, func_path, model_path):
	"""
	Classify programs and write answers to answer.txt
	:param ans_path: the path of .asm.ans files
	:param func_path: the path of .vec files
	:param model_path: the path of ResNet model and DNN model
	"""
	# Use word2vec
	files = os.listdir(ans_path)
	top_100_path = '/'.join(ans_path.split('/')[:-2]) + '/top100.txt'
	with open(top_100_path, 'r') as f:
		top100 = f.read()
		pattern = re.compile(r'[\"\'](.*?)[\"\']')
		top100_result = pattern.findall(top100)

	with open('/'.join(ans_path.split('/')[:-2])+'/answer.txt', 'w') as f:
		f.write('FileName\t\t\tCategory\n')
		for file in files:
			image_predict = [0] * 6
			vec_predict = [0] * 6

			'''--------ResNet Model--------'''
			word_model = my_word2vec(ans_path + file, 1, 5)
			if word_model is not None:
				# Convert files into matrices using top100.txt
				matrix = np.zeros((100, 100))
				for i in range(100):
					try:
						matrix[i] = word_model[top100_result[i]]
					except:
						matrix[i] = np.zeros(100)
				matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min()) * 255
				matrix = matrix.astype(np.uint8)
				matrix = matrix.reshape(1, 100, 100, 1)

				# Load ResNet model
				resnet_model = load_model(model_path + 'ResNet_model.h5')
				image_predict = resnet_model.predict(matrix)

			'''--------DNN Model--------'''
			# Convert file into .vec file
			vec_file = func_path + file.strip('.asm.ans') + '.vec'

			# Get 1*300 vector
			vec = []
			with open(vec_file, 'r') as f_vec:
				a = f_vec.readline()
				while a is not '':
					vec.append(int(a.strip()))
					a = f_vec.readline()
			vec = np.asarray(vec)

			# Load DNN model
			dnn_model = load_model(model_path + 'tf_idf_model.h5')

			if not np.all(vec[:-1] == 0):
				#print(vec,len(vec))
				vec_predict = dnn_model.predict(np.reshape(vec[0:-1], (1, len(vec[:-1]))))

			'''--------Merged Model--------'''
			resnet_weight = 0.2
			dnn_weight = 0.8

			image_predict = np.asarray(image_predict)
			vec_predict = np.asarray(vec_predict)
			#print(image_predict,vec_predict)
			merged_predict = image_predict * resnet_weight + vec_predict * dnn_weight

			category_list = ['backdoor.farfli', 'rootkit.heur', 'trojan.downloader', 'trojan.generic', 'trojan.pws', 'variant.graftor']

			y_predict = int(np.argmax(np.asarray(merged_predict)))
			print(category_list[y_predict])
			f.write(file + '\t\t\t' + category_list[y_predict] + '\n')


def evaluate(file_path, image_test_path, func_test_path, model_path):
	"""
	Evaluate model
	:param file_path: the path of files to be classified
	:param image_test_path: the path of image test files
	:param func_test_path: the path of vec test files
	:param model_path: the path of ResNet model and DNN model
	"""

	top_100_path = '/'.join(file_path.split('/')[0:-3]) + '/data/top100.txt'
	X_test_image, y_test_image, image_file_names, category_name = train.load_test_data(image_test_path, top_100_path)
	X_test_vec, y_test_vec, vec_file_names = load_data(func_test_path)

	resnet_model = load_model(model_path + 'ResNet_model.h5')
	dnn_model = load_model(model_path + 'tf_idf_model.h5')

	dirs = os.listdir(file_path)
	cnt = 0
	accuracy = 0
	sum = 0
	y = []
	y_category = [0] * 6
	y_category_predict = [0] * 6

	# Get all file names
	file_names = []
	for dir in dirs:
		files = os.listdir(file_path + dir)
		training_num = int(len(files) * 0.9)
		files = files[training_num:]
		for file in files:
			file_names.append(file.strip('.asm.ans'))
			y.append(cnt)
		cnt += 1

	for i in range(len(file_names)):
		if file_names[i] in image_file_names:
			image = X_test_image[image_file_names.index(file_names[i])]
			print(image)
			image = image[np.newaxis, :]
		else:
			image = None
		if file_names[i] in vec_file_names:
			vec = X_test_vec[vec_file_names.index(file_names[i])]
			vec = vec[np.newaxis, :]
		else:
			vec = None

		merged_predict = [0] * 6
		if image is not None and vec is not None:
			image_predict = resnet_model.predict(image)
			vec_predict = dnn_model.predict(vec)

			resnet_weight = 0.1
			dnn_weight = 0.9
                    
			merged_predict = image_predict * resnet_weight + vec_predict * dnn_weight
			y_category[y[i]] += 1
			sum += 1
		elif image is not None:
			image_predict = resnet_model.predict(image)
			merged_predict = image_predict
			y_category[y[i]] += 1
			sum += 1
		elif vec is not None:
			vec_predict = dnn_model.predict(vec)
			merged_predict = vec_predict
			y_category[y[i]] += 1
			sum += 1
		else:
			continue

		y_predict = np.argmax(np.asarray(merged_predict))

		if y_predict == y[i]:
			y_category_predict[y[i]] += 1
			accuracy += 1

	accuracy /= sum
	print('accuracy: ', accuracy)
	for i in range(6):
		print('%s \t %.2f' % (category_name[i], y_category_predict[i] / y_category[i]))


if __name__ == "__main__":
	evaluate("./data/ans/", "./resnet_test/", "./func_test/", "./model/")
