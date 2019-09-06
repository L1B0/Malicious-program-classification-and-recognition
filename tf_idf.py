from keras.layers import Dense, Input
from keras.models import Model, Sequential
from keras.utils import np_utils
from sklearn.model_selection import train_test_split

import os
import numpy as np


def generate_dataset(path):
	"""Generate non-zero vector from files"""

	x = []
	y = []
	dirs = os.listdir(path)
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
			if not np.all(vec[0:-1] == 0):
				x.append(vec[0:-1])
				y.append(cnt)

		cnt += 1

	return np.asarray(x), np.asarray(y)


def train(x, y):
	# Split the dataset
	X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

	model = Sequential()
	model.add(Dense(50, input_dim=50, activation='relu'))
	model.add(Dense(30, activation='relu'))
	model.add(Dense(30, activation='relu'))
	model.add(Dense(11, activation='softmax'))

	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

	model.fit(X_train, y_train, epochs=100)

	accuracy = model.evaluate(X_test, y_test)
	print(accuracy)


if __name__ == "__main__":
	x, y = generate_dataset('./functimes/')
	y = np_utils.to_categorical(y, 11)
	train(x, y)
