import os
import shutil


def generate_train(category, model_path, train_path):
	"""
	Select 90% files as training dataset
	:param category: the malware category
	:param model_path: the path of .asm.ans.model files
	:param train_path: the path of training dataset
	"""

	files = os.listdir(model_path + category)
	training_num = int(len(files) * 0.9)

	# Copy the training dataset to new directories
	for file in files[0: training_num]:
		shutil.move(model_path + category + '/' + file, train_path + category + '/' + file)


def generate_test(category, model_path, test_path):
	"""
	Select 10% files as test dataset
	:param category: the malware category
	:param model_path: the path of .asm.ans.model files
	:param test_path: the path of test dataset
	"""

	files = os.listdir(model_path + category)

	# Copy the test dataset to new directories
	for file in files:
		shutil.move(model_path + category + '/' + file, test_path + category + '/' + file)


def generate_dataset(model_path, train_path, test_path):
	"""
	Generate training dataset and test dataset from .asm.ans.model files
	:param model_path: the path of .asm.ans.model files
	:param train_path: the path of training dataset
	:param test_path: the path of test dataset
	"""

	if not os.path.exists(train_path):
		os.mkdir(train_path)
	if not os.path.exists(test_path):
		os.mkdir(test_path)

	category_list = os.listdir(model_path)
	for file in category_list:
		if not os.path.exists(train_path + '/' + file):
			os.mkdir(train_path + '/' + file)
		generate_train(file, model_path, train_path)

		if not os.path.exists(test_path + '/' + file):
			os.mkdir(test_path + '/' + file)
		generate_test(file, model_path, test_path)

	shutil.rmtree(model_path)


if __name__ == "__main__":
	# Please backup your dataset!!!
	generate_dataset("./data/train", "./train", "./test")
