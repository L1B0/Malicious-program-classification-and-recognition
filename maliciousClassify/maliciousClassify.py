# coding=UTF-8
#!/usr/bin/python3

import os
from maliciousClassify import batchprocess as bp
from maliciousClassify import pre,count
from tqdm import tqdm

def start(ida_path,now_pwd):

	bp.start(ida_path,now_pwd)
	asm_dic = '/'.join(now_pwd.split('/')[:-1]) + '/asm'
	pre.start(asm_dic)
	count.start('/'.join(now_pwd.split('/')[:-1]))