# coding=UTF-8
#!/usr/bin/python3

import os
from TFIDF import getApiList
from TFIDF import calcTF
from tqdm import tqdm

def start(ida_path,now_pwd):

	getApiList.start(ida_path,now_pwd)
	
	api_dic = '/'.join(now_pwd.split('/')[:-1]) + '/api'
	if os.path.exists(api_dic) == False:
		os.makedirs(api_dic)
	func_dic = '/'.join(now_pwd.split('/')[:-1]) + '/functimes'
	if os.path.exists(func_dic) == False:
		os.makedirs(func_dic)
	calcTF.start(api_dic)