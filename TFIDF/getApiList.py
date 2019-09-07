# coding=UTF-8
#!/usr/bin/python3

import os
import time
import shutil
import subprocess
from tqdm import tqdm

def start(ida_path, now_pwd):
	
	for filename in os.listdir(now_pwd):
	
		child_dic = now_pwd + '\\' + filename
		target_dic = '\\'.join(now_pwd.split('\\')[:-1]) + '\\api\\' + filename
		if os.path.exists(target_dic) == False:
			os.makedirs(target_dic)
		
		for badfile in os.listdir(child_dic):
			
			badfile_dic = child_dic + '\\' + badfile
			#badfile_dic = 'F:\\大四上\\小学期\\PE文件-文件名为家族名\\' + filename + '\\' + '.'.join(badfile.split('.')[:-1]) + '.l1b0'
			#print(badfile_dic)
			#badfile_dic = child_dic + '\\' + badfile
			if '.' in badfile:
				os.remove(badfile_dic)
				continue
			print(filename, badfile)
			
			#check = 'F:\\大四上\\小学期\\final_example_class\\api\\' + filename + '\\' + '.'.join(badfile.split('.')[:-1]) + '.api'
			check = '\\'.join(now_pwd.split('\\')[:-1]) + '\\api\\' + filename + '\\' + badfile + '.api'
			#print(check)
			if os.path.exists(check):
				continue
			cmd=[ida_path,'-B','-S"./ida.py"',badfile_dic]
			a = subprocess.Popen(cmd)
			time.sleep(1)
			'''
			# idb文件，删除

			#print("remove %s"%temp_idb)
			t1 = time.time()
			flag = False
			while not flag :
				t2 = time.time()
				if (t2-t1) > 10:
					#print("It's not pe or elf!")
					break
				try:
					os.remove(temp_dic)
					flag = True
				except:
					pass
			if not flag:
				continue
			'''


if __name__ == "__main__":

	start('C:\\Program Files (x86)\\IDA\\ida.exe','F:\\大四上\\小学期\\final_example_class\\final_example_class')