#!/usr/bin/py

import os

def install():
           os.system('sudo yum install httpd -y')
           os.system('sudo yum install mysql-server -y')
           os.system('sudo yum install php libapache2-mod-php php-mysql -y')
    
def start():
	os.system('sudo systemctl start httpd')
	os.system('sudo systemctl status httpd --no-pager')
	os.system('sudo systemctl start mysql')
	os.system('sudo systemctl status mysql --no-pager')

def stop():
	os.system('sudo systemctl stop httpd')
	os.system('sudo systemctl status httpd --no-pager')
	os.system('sudo systemctl stop mysql')
	os.system('sudo systemctl status mysql --no-pager')

def uninstall():
           os.system('sudo yum remove httpd -y')
           os.system('sudo yum remove mysql-server -y')
           os.system('sudo yum remove php libapache2-mod-php php-mysql -y')
           
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
	

    
