#!/usr/bin/py

import os

def install():
           os.system('sudo apt install apache2 -y')
           os.system('sudo apt install mysql-server -y')
           os.system('sudo apt install php libapache2-mod-php php-mysql -y')
    
def start():
	os.system('sudo systemctl start apache2')
	os.system('sudo systemctl status apache2 --no-pager')
	os.system('sudo systemctl start apache2')
	os.system('sudo systemctl status apache2 --no-pager')

def stop():
	os.system('sudo systemctl stop apache2')
	os.system('sudo systemctl status apache2 --no-pager')
	os.system('sudo systemctl stop mysql')
	os.system('sudo systemctl status mysql --no-pager')

def uninstall():
           os.system('sudo apt remove apache2')
           os.system('sudo apt remove mysql-server')
           os.system('sudo apt remove php libapache2-mod-php php-mysql')
           
print("1.Install lamp")
print("2.Start lamp")
print("3.Stop lamp")
print("4.Unistall lamp")
choice = int(input("Enter you choice: "))


if choice == 1: 
	install()
	
elif choice == 2: 
	start()
	
elif choice == 3:  
	stop()

elif choice == 4:  
	uninstall()

else:
    print("oops!")
	

    
