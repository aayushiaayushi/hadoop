#!/usr/bin/python

import os,commands,time,sys,socket,getpass

print "Welcome to world of data"
print "________________________"

print "@@@@@@@@@@@@@@@@@@@@@@@@"
print "########################"

time.sleep(2)
#Enter username to get access
user=raw_input("enter username to access project: ")

#Enter password
password=getpass.getpass("enter password:")

if user == 'root' and password == 'redhat':
	print "access granted !!!"
	execfile('menu.py')
else:
	print "****************"
	print "Wrong authentication"
	print "****************"
	
