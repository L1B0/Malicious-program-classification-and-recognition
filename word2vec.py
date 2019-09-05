from gensim.models import word2vec
import re
import os


def preprocess(min_word_count, context):
	path = "./data/ans/"
	spath = os.listdir(path)
	if not os.path.exists('./data/train/'):
		os.mkdir('./data/train')
	for pathi in spath:
		files = os.listdir(path + pathi)
		for file in files:
			f = open(path + pathi + "/" + file)
			sentences = []
			for line in f.readlines():
				sentences.append(re.sub('[^a-zA-Z]', ' ', line.lower().strip()).split())

			# 设置词语向量维度
			num_featrues = 100
			# 保证被考虑词语的最低频度
			# min_word_count = 5
			# 设置并行化训练使用CPU计算核心数量
			num_workers = 4
			# 设置词语上下文窗口大小
			# context = 5
			downsampling = 1e-3

			try:
				model = word2vec.Word2Vec(sentences, workers=num_workers, size=num_featrues, min_count=min_word_count,
				                          window=context, sample=downsampling)
			except:
				continue

			model.init_sims(replace=True)

			# 输入一个路径，保存训练好的模型，其中./data/model目录事先要存在
			if not os.path.exists('./data/train/' + pathi):
				os.mkdir('./data/train/' + pathi)
			model.save('./data/train/' + pathi + "/" + file + ".model")


if __name__ == "__main__":
	preprocess(1, 5)
