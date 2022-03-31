#!/usr/bin/python
import os
print("Your System is updating!..")
os.system('sudo apt update')
print("Your System is upgrading!..")
#os.system('sudo apt upgrade')
print("Installing git..")
os.system('sudo apt install git')
print("Check git version!..")
os.system('git --version')
print("Git is Installed Successfully.")

