from os import listdir, chdir
import re
import os

chdir("/home/pratik/Desktop/NewMonths")

for i in range(1,13):
	path=('/home/pratik/Desktop/NewMonths/%s_1998' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('/home/pratik/Desktop/NewMonths/%s_1999' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('/home/pratik/Desktop/NewMonths/%s_2000' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('/home/pratik/Desktop/NewMonths/%s_2001' % i )
	os.makedirs(path)

for i in range(1,13):
	path=('/home/pratik/Desktop/NewMonths/%s_2002' % i )
	os.makedirs(path)