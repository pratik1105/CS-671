from os import listdir, chdir
import sys
import os
chdir('/home/pratik/Desktop/NewUsers')
names = [d for d in listdir(".") if "." not in d]

for name in names:
	chdir('/home/pratik/Desktop/NewUsers/%s' %(name))
	chdir('./2002_09')
	for file in os.listdir('.'):
		if file.endswith('png'):
			os.remove(file)