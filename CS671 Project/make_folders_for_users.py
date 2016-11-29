from os import listdir, chdir
import re
import os


chdir("/home/pratik/Desktop/maildir")
names = [d for d in listdir(".") if "." not in d]

chdir("/home/pratik/Desktop/Users")
for name in names:
	os.makedirs('/home/pratik/Desktop/Users/%s' % name)
	for i in range(1,13):
	    path=('/home/pratik/Desktop/Users/%s/%s_1998' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('/home/pratik/Desktop/Users/%s/%s_1999' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('/home/pratik/Desktop/Users/%s/%s_2000' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('/home/pratik/Desktop/Users/%s/%s_2001' % (name,i) )
	    os.makedirs(path)

	for i in range(1,13):
	    path=('/home/pratik/Desktop/Users/%s/%s_2002' % (name,i) )
	    os.makedirs(path)