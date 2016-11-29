from os import chdir,listdir
import re
import os

chdir("/home/pratik/Desktop/nlp/Brown-data/train/")
names = [d for d in listdir(".") if "." not in d]


for name in names:
	f=open('%s' %(name),'r')
	w=open('/home/pratik/Desktop/nlp/Brown-data/Tag_sequence/%s' %(name),'w')
	
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			if b=='.':
				w.write("STOP"+" ")
			else:
				w.write(b+" ")