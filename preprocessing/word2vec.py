from gensim.models import word2vec

import re
import os


def my_word2vec(path, min_count, context):
	"""
	convert words to vectors with dimension 100
	:param path: the path of file to be vectorized
	:param min_count: min frequency of word to be considered
	:param context: the size of context window
	:return: Word2Vec model
	"""

	f = open(path, 'r')
	sentences = []
	for line in f.readlines():
		sentences.append(re.sub('[^a-zA-Z]', ' ', line.lower().strip()).split())

	try:
		model = word2vec.Word2Vec(sentences, workers=4, size=100, min_count=min_count, window=context,
		                          sample=1e-3)
	except:
		return None

	model.init_sims(replace=True)

	return model


def batch_vectorize_asm(asm_path, model_path):
	"""
	vectorize the training dataset
	:param asm_path: the path of .ans files
	:param model_path: the path of .ans.model files
	"""
	if not os.path.exists(model_path):
		os.mkdir(model_path)

	dirs = os.listdir(asm_path)

	for dir in dirs:
		files = os.listdir(asm_path + dir)
		for file in files:
			model = my_word2vec(asm_path + dir + '/' + file, 1, 5)
			if model is not None:
				if not os.path.exists(model_path + dir):
					os.mkdir(model_path + dir)
				model.save(model_path + dir + "/" + file + ".model")


if __name__ == "__main__":
	batch_vectorize_asm("./data/ans/", "./data/train/")
