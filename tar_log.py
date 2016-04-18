#!/usr/bin/python3.2
#--encoding-uf8--
import os
import tarfile
import shutil
import datetime
import time
import sys

pro=[]
for file in os.system('ls -d /tmp'):
    pro=pro.__add__(file)