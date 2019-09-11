# coding=UTF-8
#!\\usr\\bin\\python3

import os
import time
import shutil
import subprocess

cmd=['C:\\Program Files (x86)\\IDA\\ida.exe','-B','-S"./ida.py"','F:\\大四上\\小学期\\final_example_class\\test\\test1\\test_files\\Virusshare_00c1c2568c63b25734f292716a296d90']
a = subprocess.Popen(cmd)