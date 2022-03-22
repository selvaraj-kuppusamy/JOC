#!/usr/bin/py
import os
print("creating seven directories!")
mutipledirs = ['ubuntu','centos','redhat','fedora','kalilinux','Opensuse']
for order in mutipledirs:
	os.mkdir(order)
print("Seven directories are created")
print("Let's Check!")
cmd = 'ls'
os.system(cmd)
