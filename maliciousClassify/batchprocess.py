# coding=UTF-8
#!/usr/bin/python3

import os
import time
import shutil
import subprocess
from tqdm import tqdm

def myinput(now_pwd):
	
	malicious_dic = now_pwd + '\\malicious'
	asm_dic = now_pwd + '\\asm'
	return malicious_dic,asm_dic

def start(ida_path, now_pwd):
	
	print("Start disasm~")
	num = 0
	#parent_dic = "F:\\大四上\\小学期\\final_example_class\\final_example_class"
	malicious_dic, asm_dic = myinput(now_pwd)
	
	for filename in os.listdir(malicious_dic):
	
		#print(filename)
		child_dic = malicious_dic + '\\' + filename
		target_dic = asm_dic + '\\' + filename
		
		if os.path.exists(target_dic) == False:
			os.makedirs(target_dic)
		
		for badfile in tqdm(os.listdir(child_dic), desc=filename):

			badfile_dic = child_dic + '\\' + badfile
			
			temp = badfile.split('.')[:-1]
			temp_asm = '.'.join(temp) + '.asm'
			temp_dic = target_dic + '\\' + temp_asm
			if os.path.exists(temp_dic):
				#print("pass %s~"%temp_asm)
				continue
			
			num += 1
			#print("[%d]create %s.asm"%(num,badfile))
			cmd=[ida_path,'-B',badfile_dic]
			a = subprocess.Popen(cmd)
			
			temp_idb = badfile + '.idb'
			temp_asm = badfile + '.asm'
			
			temp_dic = child_dic + '\\' + temp_idb
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
			
			temp_dic = child_dic + '\\' + temp_asm
			# asm文件，移动
			#print("move %s"%temp_asm)
			t1 = time.time()
			flag = False
			while not flag :
				t2 = time.time()
				if (t2-t1) > 10:
					#print("It's not pe or elf!")
					break
				try:
					shutil.move(child_dic + '\\' + temp_asm, target_dic + '\\' + temp_asm)
					flag = True
				except:
					pass
				
		
				
			
			
			

		
				
			
		







