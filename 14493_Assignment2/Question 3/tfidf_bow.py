import nltk
from os import chdir,listdir
import re
import os
import numpy as np

train_review_pos=[]
train_review_neg=[]
chdir("/home/pratik/Desktop/nlp/Imdb-data/train/pos")
names=[]
names = [d for d in listdir(".")]

for name in names:
	f=open('%s' %(name),'r')
	templist=[]
	for word in f.read().split():
		templist.append(word.lower())
	train_review_pos.append(" ".join(templist))
	f.close()

chdir("/home/pratik/Desktop/nlp/Imdb-data/train/neg")
new_names=[]
new_names= [d for d in listdir(".") if d.endswith('txt')]

for name in new_names:
	f=open('%s' %(name),'r')
	templist=[]
	for word in f.read().split():
		templist.append(word.lower())
	train_review_neg.append(" ".join(templist))


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
vectorizer= CountVectorizer(analyzer="word",tokenizer=None,preprocessor=None,stop_words='english',max_features=5000)
train_data_features_pos=vectorizer.fit_transform(train_review_pos)
train_data_features_neg=vectorizer.fit_transform(train_review_neg)
transformer=TfidfTransformer(smooth_idf=False)
tfidf_pos=transformer.fit_transform(train_data_features_pos)
tfidf_neg=transformer.fit_transform(train_data_features_neg)

tfidf_neg=tfidf_neg.toarray()
tfidf_pos=tfidf_pos.toarray()
#print len(train_data_features_pos)
#print len(train_data_features_neg)

'''for lst in train_data_features_pos:
	for i in range(0,len(lst)):
		if lst[i]>0:
			lst[i]=1

for lst in train_data_features_neg:
	for i in range(0,len(lst)):
		if lst[i]>0:
			lst[i]=1
'''
combined=[]
for lst in tfidf_pos:
	combined.append(lst)
for lst in tfidf_neg:
	combined.append(lst)

from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(n_estimators=100)

sentiments=[]
for i in range(12500):
	sentiments.append(1)
for i in range(12500):
	sentiments.append(0);



forest=forest.fit(combined,sentiments)

test_review_pos=[]
test_review_neg=[]
chdir("/home/pratik/Desktop/nlp/Imdb-data/test/pos")
names=[]
names = [d for d in listdir(".")]

for name in names:
	f=open('%s' %(name),'r')
	templist=[]
	for word in f.read().split():
		templist.append(word.lower())
	test_review_pos.append(" ".join(templist))

chdir("/home/pratik/Desktop/nlp/Imdb-data/test/neg")
new_names=[]
new_names= [d for d in listdir(".")]

for name in new_names:
	f=open('%s' %(name),'r')
	templist=[]
	for word in f.read().split():
		templist.append(word.lower())
	test_review_neg.append(" ".join(templist))


vectorizer= CountVectorizer(analyzer="word",tokenizer=None,preprocessor=None,stop_words='english',max_features=5000)
test_data_features_pos=vectorizer.fit_transform(test_review_pos)
test_data_features_neg=vectorizer.fit_transform(test_review_neg)
test_tfidf_pos=transformer.fit_transform(test_data_features_pos)
test_tfidf_neg=transformer.fit_transform(test_data_features_neg)

test_tfidf_neg=test_tfidf_neg.toarray()
test_tfidf_pos=test_tfidf_pos.toarray()

'''for lst in test_data_features_pos:
	for i in range(0,len(lst)):
		if lst[i]>0:
			lst[i]=1

for lst in test_data_features_neg:
	for i in range(0,len(lst)):
		if lst[i]>0:
			lst[i]=1
'''

result_pos=forest.predict(test_tfidf_pos)
result_neg=forest.predict(test_tfidf_neg)

count=0
for i in result_pos:
			if i==1:
				count+=1

for i in result_neg:
	if i==0:
		count+=1

accuracy=float(count)/(len(result_neg)+len(result_neg))
print accuracy