import os
import shutil


def generate_train(category):
	"""
	Select 90% files as training dataset
	:param: category: the malware category
	"""

	src = './data/train'
	train_dest = './train'
	files = os.listdir(src + '/' + category)
	training_num = int(len(files) * 0.9)

	# Move the training dataset to new directories
	for file in files[0: training_num]:
		shutil.move(src + '/' + category + '/' + file, train_dest + '/' + category + '/' + file)


def genetare_test(category):
	"""
	Select 10% files as test dataset
	:param category: the malware category
	"""

	src = './data/train'
	test_dest = './test'
	files = os.listdir(src + '/' + category)

	# Move the test dataset to new directories
	for file in files:
		shutil.move(src + '/' + category + '/' + file, test_dest + '/' + category + '/' + file)


def generate_dataset():
	src = './data/train'
	train_dest = './train'
	test_dest = './test'
	if not os.path.exists(train_dest):
		os.mkdir(train_dest)

	if not os.path.exists(test_dest):
		os.mkdir(test_dest)

	category_list = os.listdir(src)
	for file in category_list:
		if not os.path.exists(train_dest + '/' + file):
			os.mkdir(train_dest + '/' + file)
		generate_train(file)

		if not os.path.exists(test_dest + '/' + file):
			os.mkdir(test_dest + '/' + file)
		genetare_test(file)

	shutil.rmtree('./data/train')


if __name__ == "__main__":
	generate_dataset()
