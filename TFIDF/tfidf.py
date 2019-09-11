# coding=UTF-8
#!/usr/bin/python3

import os
from TFIDF import getApiList
from TFIDF import calcTF
from tqdm import tqdm

def start(ida_path,idapy_path,now_pwd):

	# get import api list
	api_dic = '/'.join(now_pwd.split('/')[:-1]) + '/api'
	if os.path.exists(api_dic) == False:
		os.makedirs(api_dic)
	getApiList.start(ida_path,now_pwd)
	
	# calculate TF-IDF
	func_dic = '/'.join(now_pwd.split('/')[:-1]) + '/functimes'
	if os.path.exists(func_dic) == False:
		os.makedirs(func_dic)
	calcTF.start(api_dic)

def predict(ida_path,idapy_path,now_pwd,topapi_path):

	# get import api list
	api_dic = '/'.join(now_pwd.split('/')[:-1]) + '/api'
	if os.path.exists(api_dic) == False:
		os.makedirs(api_dic)
	getApiList.start(ida_path,idapy_path,now_pwd)
	
	# predict
	func_dic = '/'.join(now_pwd.split('/')[:-1]) + '/functimes'
	if os.path.exists(func_dic) == False:
		os.makedirs(func_dic)
	calcTF.predict(api_dic,topapi_path)