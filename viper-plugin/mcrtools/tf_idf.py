from keras.layers import Dense, Dropout
from keras.models import Sequential, save_model
from keras.optimizers import SGD
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils

from sklearn.model_selection import GridSearchCV, StratifiedKFold

from .preprocessing.generate_dataset import generate_dataset

import os
import numpy as np


def load_data(path):
	"""Generate non-zero vector from files"""

	x = []
	y = []
	file_names = []
	vec_len = 0
	dirs = os.listdir(path)
	cat_len = len(dirs)
	#print("cate: %d"%cat_len)
	cnt = 0
	for category in dirs:
		files = os.listdir(path + category)
		for file in files:
			vec = []
			with open(path + category + '/' + file, 'r') as f:
				a = f.readline()
				while a is not '':
					vec.append(int(a.strip()))
					a = f.readline()
			vec = np.asarray(vec)
			vec_len = len(vec[:-1])
			if not np.all(vec[0:-1] == 0):
				x.append(vec[0:-1])
				y.append(cnt)
				file_names.append(file.strip('.vec'))

		cnt += 1

	return np.asarray(x), np.asarray(y), file_names, vec_len, cat_len


def create_model(layer1, layer2, layer3, dropout, vec_len, cat_len):
	# DNN Model
	model = Sequential()
	model.add(Dense(layer1, input_dim=vec_len, activation='relu'))
	model.add(Dense(layer2, activation='relu'))
	model.add(Dense(layer3, activation='relu'))
	model.add(Dropout(dropout))
	model.add(Dense(cat_len, activation='softmax'))

	model.compile(loss='categorical_crossentropy', optimizer="adam", metrics=['accuracy'])

	return model


def train(X_train, y_train, X_test, y_test, model_path, vec_len, cat_len):
	y_train = np_utils.to_categorical(y_train, cat_len)
	y_test = np_utils.to_categorical(y_test, cat_len)

	model = create_model(500, 750, 250, 0.4, vec_len, cat_len)
	# model = KerasClassifier(build_fn=create_model, batch_size=1, verbose=1)

	'''
	# Parameter list
	layer1_num_list = [500]
	layer2_num_list = [750]
	layer3_num_list = [250]
	dropout_rate_list = [0.4]
	epochs = [300]

	param_grid = dict(layer1=layer1_num_list, layer2=layer2_num_list, layer3=layer3_num_list, dropout=dropout_rate_list,
	                  nb_epoch=epochs)
	grid = GridSearchCV(estimator=model, param_grid=param_grid, n_jobs=1)

	grid_result = grid.fit(X_train, y_train)

	print("Best accuracy: %.2f\n using %s" % (grid_result.best_score_, grid_result.best_params_))
	'''

	model.fit(X_train, y_train, batch_size=28, epochs=100)

	if not os.path.exists(model_path):
		os.mkdir(model_path)
	save_model(model, model_path + 'tf_idf_model.h5')

	accuracy = model.evaluate(X_test, y_test)
	print(accuracy)


def cross_validation(x, y):
	model = create_model(500, 750, 250, 0.4, vec_len, cat_len)
	skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=10)
	cv = []

	for train_index, test_index in skf.split(x, y):
		X_train, X_test = x[train_index], x[test_index]
		y_train, y_test = y[train_index], y[test_index]
		y_train = np_utils.to_categorical(y_train, cat_len)
		y_test = np_utils.to_categorical(y_test, cat_len)

		model.fit(X_train, y_train, batch_size=28, epochs=100)

		accuracy = model.evaluate(X_test, y_test)
		print('accuracy: %.2f%%' % accuracy[1] * 100)
		cv.append(accuracy[1] * 100)

	cv = np.asarray(cv)
	print('average accuracy: %.2f' % np.mean(cv))


def train_dnn(training_path, test_path, model_path):
	"""
	Train DNN model and save it
	:param training_path: the path of training dataset
	:param test_path: the path of test dataset
	:param model_path: the path of DNN model
	"""

	X_train, y_train, _, vec_len, cat_len = load_data(training_path)
	X_test, y_test, _, vec_len, cat_len = load_data(test_path)
	train(X_train, y_train, X_test, y_test, model_path, vec_len, cat_len)


if __name__ == "__main__":
	generate_dataset("./data/functimes/", "./func_train", "./func_test")
	train_dnn("./func_train/", "./func_test/", "../model/")
# cross_validation(X_test, y_test)
