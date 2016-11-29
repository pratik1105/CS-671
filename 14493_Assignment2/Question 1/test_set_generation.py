from os import chdir,listdir
import re


chdir("/home/pratik/Desktop/nlp/Brown-data/brown/")
names = [d for d in listdir(".") if "." not in d]

for name in names:
	f=open('%s' %(name),'r')
	w=open('/home/pratik/Desktop/nlp/Brown-data/test/%s' %(name),'w')
	#print name
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			w.write(a+" ")              