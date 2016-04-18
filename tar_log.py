#!/usr/bin/python3.2
#--encoding-uf8--
import os
import tarfile
import shutil
import datetime
import time
import sys

pro=[]
for root,dir,files in os.walk('/tmp/'):
    for file in files:
        pro=pro.append(file)