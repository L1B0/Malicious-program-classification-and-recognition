# coding=UTF-8
#!/usr/bin/python3

import os
import batchprocess as bp 
import pre,count
from tqdm import tqdm

def start(ida_path,now_pwd):

	bp.start(ida_path,now_pwd)
	asm_dic = '/'.join(now_pwd.split('/')[:-1]) + '/asm'
	if os.path.exists(asm_dic) == False:
		os.makedirs(asm_dic)
	pre.start(asm_dic)
	ans_dic = '/'.join(now_pwd.split('/')[:-1]) + '/ans'
	if os.path.exists(ans_dic) == False:
		os.makedirs(ans_dic)
	count.start(ans_dic)
