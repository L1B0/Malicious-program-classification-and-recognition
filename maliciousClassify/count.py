import json
import os

def save(dict,path):
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
	path = now_pwd + "//ans"
	number = 0
	dict={}
	for (root, dirs, files) in os.walk(path):
		for filename in files:
			print(filename)
				
			count(os.path.join(root,filename),dict)
		save(dict,now_pwd + '//count.txt')
