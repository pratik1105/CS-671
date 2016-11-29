from os import chdir,listdir
import re
import os

tag_for={}
new_tags={}
chdir("/home/pratik/Desktop/nlp/Brown-data/")
f=open('Learned_tags_by_freq','r')


for word in f.read().split():
	a,b=word.split('/')
	tag_for[a]=b


chdir("/home/pratik/Desktop/nlp/Brown-data/test")
names = [d for d in listdir(".") if "." not in d]

for name in names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
		if word in tag_for:
			new_tags[word]=tag_for[word]
		else:
			new_tags[word]='nn'



chdir("/home/pratik/Desktop/nlp/Brown-data/Correct")
new_names= [d for d in listdir(".") if "." not in d]
 
right=0
wrong=0 
for name in new_names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			if b == new_tags[a]:
				right=right+1
			else:
				wrong=wrong+1

print("accuracy with frequency tagging is %f percent." %(100*float(right)/(right+wrong)))