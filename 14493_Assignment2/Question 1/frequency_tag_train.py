from os import chdir,listdir
import re
import os

chdir("/home/pratik/Desktop/nlp/Brown-data/train")
names = [d for d in listdir(".") if "." not in d]
print names[:2]

map1={}
map2={}
max_freq={}
count1=0
count2=0
w=50000
h=500
Matrix = [[0 for x in range(h)] for y in range(w)]
print len(Matrix) 
vocab=set()
tag_set=set()
for name in names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			vocab.add(a)
			tag_set.add(b)
			if not (a in map1):
				map1[a]=count1
				count1=count1+1
			if not (b in map2):
				map2[b]=count2
				count2=count2+1

print(count1)
print(count2)				

for name in names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			Matrix[map1[a]][map2[b]]=Matrix[map1[a]][map2[b]]+1

chdir("/home/pratik/Desktop/nlp/Brown-data/")
f=open('Learned_tags_by_freq','w');
for word in vocab:
	freq=0;
	for tag in tag_set:
		if Matrix[map1[word]][map2[tag]]>freq:
			freq=Matrix[map1[word]][map2[tag]]
			max_freq[word]=tag
	f.write("%s/%s" %(word,max_freq[word]) + '\n')
    
