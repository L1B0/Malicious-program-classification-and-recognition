# coding=UTF-8
#!/usr/bin/python3

import os
from maliciousClassify import batchprocess as bp
from maliciousClassify import pre,count
from tqdm import tqdm

def start(ida_path,now_pwd):

	bp.start(ida_path,now_pwd)
	pre.start(now_pwd)
	count.start(now_pwd)