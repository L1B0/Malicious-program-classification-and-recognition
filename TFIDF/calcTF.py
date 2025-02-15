# coding=UTF-8
#!/usr/bin/python3

import os
import numpy as np
from sklearn import feature_extraction    
from sklearn.feature_extraction.text import TfidfTransformer    
from sklearn.feature_extraction.text import CountVectorizer

def start(now_pwd):
	
	all_top = []
	for filename in os.listdir(now_pwd):
	
		child_dic = now_pwd + '/' + filename
		
		func_name_list = []
		temp = []
		top = []
		for badfile in os.listdir(child_dic):
			
			#print("Read %s"%badfile)
			badfile_dic = child_dic + '/' + badfile
			
			a = eval(open(badfile_dic,'r').read())
			if a == []:
				continue
			temp.append(a)
			a = ' '.join(a)
			func_name_list.append(a)
		'''
		with open('func_name_list','w') as f:
			for i in func_name_list:
				f.write(i)
		'''	
		# calc TF-IDF
		vectorizer = CountVectorizer() 
		
		#该类会统计每个词语的tf-idf权值  
		transformer = TfidfTransformer() 
		
		#第一个fit_transform是计算tf-idf 第二个fit_transform是将文本转为词频矩阵  
		X = vectorizer.fit_transform(func_name_list)
		counts = X.toarray()
		#print(counts)
			
		word = vectorizer.get_feature_names()  
		#np.savetxt('word',word)
		tfidf = transformer.fit_transform(X)
		weight = tfidf.toarray()
		'''
		with open("tf-idf",'w') as f:
			for i in weight:
				for j in i:
					f.write(str(j)+' ')
				f.write('\n')
		print(weight)
		'''
		
		# 二维压缩为一维
		final_weight = np.zeros(len(weight[0]),dtype=np.float)
		for i in range(len(weight)):
			for j in range(len(weight[i])):
				final_weight[j] += weight[i][j]
		#print(final_weight)
	
		#find top wei
		wei = 20
		while 1:
			if len(top) == wei:
				break
			#index = np.argmax(weight, axis=1)
			index = np.argmax(final_weight)
			if final_weight[index] == 0:
				break
			top.append(word[index])
			final_weight[index] = 0
			if word[index] not in all_top:
				all_top.append(word[index])

		print(top)
	#print(top)
	#np.savetxt('top',top)
	with open('/'.join(now_pwd.split('/')[:-1])+'/topapi.txt','w') as f:
		f.write(str(all_top))
	
	print(len(all_top),all_top)
	# 生成每个样本的向量矩阵
	
	wei = len(all_top)
	v = np.zeros((wei+1), dtype=np.int)
	v[wei] = 1
	n = 0
	num = 0
	for filename in os.listdir(now_pwd):
	
		child_dic = now_pwd + '/' + filename
		target_dic = '/'.join(now_pwd.split('/')[:-1]) + '/functimes/' + filename
		if os.path.exists(target_dic) == False:
			os.makedirs(target_dic)
			
		for badfile in os.listdir(child_dic):
			
			#print("Read %s"%badfile)
			badfile_dic = child_dic + '/' + badfile
			
			a = eval(open(badfile_dic,'r').read())
			#print(a)
			if a == []:
				np.savetxt(target_dic+'/'+'.'.join(badfile.split('.')[:-1]) + '.vec',v,fmt='%d')
				continue
			num += 1
			temp_v = np.zeros((wei+1), dtype=np.int)
			temp_v[wei] = 1
			f = 0
			for i in range(len(all_top)):

				if all_top[i] in a:
					f = 1
					#print("get it.")
					temp_v[i] = 1

			#print(temp_v)
			if f:
				n += 1
				print("Get %d %s"%(n,badfile))
			np.savetxt(target_dic+'/'+'.'.join(badfile.split('.')[:-1]) + '.vec',temp_v,fmt='%d')		
	#print(num)			

def predict(now_pwd,topapi_path):

	all_top = eval(open(topapi_path,'r').read())
	wei = len(all_top)
	n = 0
	for filename in os.listdir(now_pwd):
	
		child_dic = now_pwd + '/' + filename
		target_dic = '/'.join(now_pwd.split('/')[:-1]) + '/functimes/' + filename
		if os.path.exists(target_dic) == False:
			os.makedirs(target_dic)
			
		for badfile in os.listdir(child_dic):
			
			#print("Read %s"%badfile)
			badfile_dic = child_dic + '/' + badfile
			
			a = eval(open(badfile_dic,'r').read())
			#print(a)
			if a == []:
				np.savetxt(target_dic+'/'+'.'.join(badfile.split('.')[:-1]) + '.vec',v,fmt='%d')
				continue
			#num += 1
			temp_v = np.zeros((wei+1), dtype=np.int)
			temp_v[wei] = 1
			f = 0
			for i in range(len(all_top)):

				if all_top[i] in a:
					f = 1
					#print("get it.")
					temp_v[i] = 1

			#print(temp_v)
			if f:
				n += 1
				print("Get %d %s"%(n,badfile))
			np.savetxt(target_dic+'/'+'.'.join(badfile.split('.')[:-1]) + '.vec',temp_v,fmt='%d')		
	#print(num)

if __name__ == "__main__":

	start('F:/大四上/小学期/final_example_class/api')
