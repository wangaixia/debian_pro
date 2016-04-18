#!/usr/bin/python3.2
#--encoding:utf-8--
import os
import tarfile
import shutil
import datetime
import time
import sys

INPUT = input("place input something: ")
pro = []
for dirpath, dirnames, filenames in os.walk('/tmp'):
    pro.extend(filenames)
    break
if INPUT in pro:
    print("exits")
else:
    print("no exits")