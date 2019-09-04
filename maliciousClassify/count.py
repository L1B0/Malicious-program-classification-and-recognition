import json
import os
from tqdm import tqdm

def save(dict,path):
    dict = sorted(zip(dict.values(),dict.keys()),reverse=True)
    with open(path,'w') as f:
        json.dump(dict,f)


def count(filepath,dict):
    with open(filepath,'r') as f:
        for line in f.readlines():
            words=line.split()
            for word in words:
                if word in dict.keys():
                    dict[word]+=1
                else:
                    dict[word]=1

def start(now_pwd):

	print("Start count~")
	path = now_pwd + "//ans"
	number = 0
	dict={}
	for (root, dirs, files) in os.walk(path):
		for filename in tqdm(files,desc=root.split('\\')[-1]):
			#print(filename)
			
			count(os.path.join(root,filename),dict)
		save(dict,now_pwd + '//count.txt')
