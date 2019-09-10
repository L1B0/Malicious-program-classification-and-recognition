#!/usr/bin/env python
# coding=utf-8

import os
import shutil

def backup(path):
        t = path.split('/')
        target_path = '/'.join(t[:-2]) + '/backup_' + t[-2] + '/'

        for dic in os.listdir(path):
            child_path = path + dic
            tchild_path = target_path + dic
            if os.path.exists(tchild_path) == False:
                os.makedirs(tchild_path)
            for filename in os.listdir(child_path):
                shutil.copyfile(child_path+'/'+filename,tchild_path+'/'+filename)


def backup2(path):
        t = path.split('/')
        target_path = '/'.join(t[:-2]) + '/backup_' + t[-2] + '/'
        if os.path.exists(target_path) == False:
            os.makedirs(target_path)
        for dic in os.listdir(path):
            child_path = path + dic
            tchild_path = target_path + dic

            shutil.copyfile(child_path,tchild_path)