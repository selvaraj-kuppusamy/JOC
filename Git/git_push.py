#!/bin/usr/py
import os
print("Checking git status")
os.system('git status')
print("Add git status")
os.system('git add .')
print("Again add git status")
os.system('git status')
print("git commiting")
os.system('git commit -m "python scripts"')
