from os import chdir,listdir
import re
import os

map1={}
map2={}
count=2
h=500
k=50000
chdir("/home/pratik/Desktop/nlp/Brown-data/Tag_sequence")
names = [d for d in listdir(".") if "." not in d]

FREQ3 = [[[0 for x in range(h)] for y in range(h)] for z in range(h)]
FREQ2 = [[0 for x in range(h)] for y in range(h)]
FREQ  = [0 for x in range(h)]
FREQP = [[0 for x in range(h)] for y in range(k)]
ans   = [[[0 for x in range(h)] for y in range(h)] for z in range(h)]
bptr  = [[[0 for x in range(h)] for y in range(h)] for z in range(h)]

map1['START']=0
map1['STOP']=1

for name in names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
			if not (word in map1):
				map1[word]=count
				count=count+1

print(count)

word1='START'
word2='START'
FREQ2[map1[word1]][map1[word2]]=+1
FREQ[map1[word1]]=+1
FREQ[map1[word2]]=+1

for name in names:
	f=open('%s' %(name),'r')
	for line in f.readline():
		word1='START'
		word2='START'
		FREQ2[map1[word1]][map1[word2]]=+1
		FREQ[map1[word1]]=+1
		FREQ[map1[word2]]=+1
		for word in line.split():
			FREQ3[map1[word1]][map1[word2]][map1[word]]+=1
			FREQ2[map1[word2]][map1[word]]+=1
			FREQ[map1[word]]+=1
			word1=word2
			word2=word

chdir("/home/pratik/Desktop/nlp/Brown-data/train")
new_names = [d for d in listdir(".") if "." not in d]

count=0

for name in new_names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			if not (a in map2):
				map2[a]=count
				count=count+1

print(count)

for name in new_names:
	f=open('%s' %(name),'r')
	for word in f.read().split():
		if word.count('/')==1:
			a,b=word.split('/')
			if b=='.':
				b='STOP'
			FREQP[map2[a]][map1[b]]+=1


chdir("/home/pratik/Desktop/nlp/Brown-data/test")
files=[d for d in listdir(".") if "." not in d]

for file in files:
	f=open('%s' %(name),'r')
	for line in f.readline():
		word1='START'
		word2='START'
		ans[0][map1['START']][map1['START']]=1
		length=size(line.split())
		



