from os import chdir,listdir
import re
import os
import nltk

chdir("/home/pratik/Desktop/nlp/Brown-data/train")
names = [d for d in listdir(".") if "." not in d]

train_sents=[]
test_sents=[]
count=0
for name in names:
	f=open('%s' %(name),'r')
	for line in f.readlines():
		s=[]
		for word in line.split():
			if word.count('/')==1:
				a,b=word.split('/')
				#print(a)
				#print(b)
				s.append((a,b))
		if s:
			train_sents.append(s)

chdir("/home/pratik/Desktop/nlp/Brown-data/Correct")
new_names = [d for d in listdir(".") if "." not in d]


for name in new_names:
	f=open('%s' %(name),'r')
	for line in f.readlines():
		s=[]
		for word in line.split():
			if word.count('/')==1:
				a,b=word.split('/')
				s.append((a,b))
		if s:
			test_sents.append(s)

unigram_tagger=nltk.UnigramTagger(train_sents)
print("%f percent accuracy with nltk tagger" %(100*unigram_tagger.evaluate(test_sents)))
#print(test_sents[2])