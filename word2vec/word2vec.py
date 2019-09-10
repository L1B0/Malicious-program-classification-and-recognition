# coding=UTF-8
#!/usr/bin/python3

import os
from word2vec import batchprocess as bp 
from word2vec import pre,count
from tqdm import tqdm

def start(ida_path,now_pwd):

	# 反汇编 
	asm_dic = '/'.join(now_pwd.split('/')[:-1]) + '/asm'
	if os.path.exists(asm_dic) == False:
		os.makedirs(asm_dic)
	bp.start(ida_path,now_pwd)

	# asm2word
	pre.start(asm_dic)
	if os.path.exists(ans_dic) == False:
		os.makedirs(ans_dic)
	ans_dic = '/'.join(now_pwd.split('/')[:-1]) + '/ans'

	# count Top100
	count.start(ans_dic)

def predict(ida_path,now_pwd):

	# 反汇编 
	asm_dic = '/'.join(now_pwd.split('/')[:-1]) + '/asm'
	if os.path.exists(asm_dic) == False:
		os.makedirs(asm_dic)
	bp.start(ida_path,now_pwd)

	# asm2word
	pre.start(asm_dic)
	if os.path.exists(ans_dic) == False:
		os.makedirs(ans_dic)
	ans_dic = '/'.join(now_pwd.split('/')[:-1]) + '/ans'
