# -*- coding: utf-8 -*-
import nltk
from os import chdir,listdir
import re
import os
import numpy as np
import gensim
from nltk.corpus import stopwords

import re
caps = "([A-Z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + caps + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(caps + "[.]" + caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(caps + "[.]" + caps + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + caps + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

train_sentences=[]

chdir("/home/pratik/Desktop/nlp/Imdb-data/train/pos_red")
names=[]
names = [d for d in listdir(".") if d.endswith('txt')]

for name in names:
    f=open('%s' %(name),'r')
    review=f.read()
    train_sentences+=split_into_sentences(review)

chdir("/home/pratik/Desktop/nlp/Imdb-data/train/neg_red")
new_names=[]
new_names= [d for d in listdir(".") if d.endswith('txt')]

for name in new_names:
    f=open('%s' %(name),'r')
    review=f.read()
    train_sentences+=split_into_sentences(review)

train_sentences_final=[]
for sentences in train_sentences:
    sentences = re.sub("[^a-zA-Z]"," ", sentences)
    words=sentences.lower().split()
    stops=set(stopwords.words("english"))
    words=[w for w in words if not w in stops]
    if len(words)>0:
        train_sentences_final.append(words)

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',level=logging.INFO)

num_features = 60    # Word vector dimensionality                      
min_word_count = 40   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

from gensim.models import word2vec
print "Training model..."
model = word2vec.Word2Vec(train_sentences_final, workers=num_workers, \
            size=num_features, min_count = min_word_count, \
            window = context, sample = downsampling)

model.init_sims(replace=True)

index2word_set=set(model.index2word)

train_review=[]
chdir("/home/pratik/Desktop/nlp/Imdb-data/train/pos_red")
names=[]
names = [d for d in listdir(".") if d.endswith('txt')]

for name in names:
    f=open('%s' %(name),'r')
    templist=[]
    for word in f.read().split():
        templist.append(word.lower())
    train_review.append(" ".join(templist))
    f.close()

chdir("/home/pratik/Desktop/nlp/Imdb-data/train/neg_red")
new_names=[]
new_names= [d for d in listdir(".") if d.endswith('txt')]

for name in new_names:
    f=open('%s' %(name),'r')
    templist=[]
    for word in f.read().split():
        templist.append(word.lower())
    train_review.append(" ".join(templist))


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

vectorizer= CountVectorizer(analyzer="word",binary=True,tokenizer=None,preprocessor=None,stop_words='english',max_features=500)
train_data_features=vectorizer.fit_transform(train_review)
vocab=vectorizer.get_feature_names()
transformer=TfidfTransformer(smooth_idf=False)
tfidf=transformer.fit_transform(train_data_features)
tfidf=tfidf.toarray()

train_vectors=[]
for lst in tfidf:
    temp_vectors=[]
    for i in range(0,len(lst)):
        if lst[i]>0 and (vocab[i] in index2word_set):
            to_add=model[vocab[i]]
            for k in range(60):
                temp_vectors.append(lst[i]*to_add[k])
        else:
            for k in range(60):
                temp_vectors.append(0)
    train_vectors.append(temp_vectors)

test_review=[]
chdir("/home/pratik/Desktop/nlp/Imdb-data/test/pos_red")
names=[]
names = [d for d in listdir(".") if d.endswith('txt')]

for name in names:
    f=open('%s' %(name),'r')
    templist=[]
    for word in f.read().split():
        templist.append(word.lower())
    test_review.append(" ".join(templist))
    f.close()

chdir("/home/pratik/Desktop/nlp/Imdb-data/test/neg_red")
new_names=[]
new_names= [d for d in listdir(".") if d.endswith('txt')]

for name in new_names:
    f=open('%s' %(name),'r')
    templist=[]
    for word in f.read().split():
        templist.append(word.lower())
    test_review.append(" ".join(templist))



vectorizer= CountVectorizer(analyzer="word",binary=True,tokenizer=None,preprocessor=None,stop_words='english',max_features=500)
test_data_features=vectorizer.fit_transform(test_review)
#vocab=vectorizer.get_feature_names()
transformer=TfidfTransformer(smooth_idf=False)
test_tfidf=transformer.fit_transform(test_data_features)
test_tfidf=test_tfidf.toarray()

test_vectors=[]
for lst in test_tfidf:
    temp_vectors=[]
    for i in range(0,len(lst)):
        if lst[i]>0 and (vocab[i] in index2word_set):
            to_add=model[vocab[i]]
            for k in range(60):
                temp_vectors.append(lst[i]*to_add[k])
        else:
            for k in range(60):
                temp_vectors.append(0)

    test_vectors.append(temp_vectors)

from sklearn.ensemble import RandomForestClassifier
forest=RandomForestClassifier(n_estimators=100)

sentiments=[]
for i in range(1500):
    sentiments.append(1)
for i in range(1500):
    sentiments.append(0);


forest=forest.fit(train_vectors,sentiments)
result=forest.predict(test_vectors)
count=0
for i in range(0,1500):
    if result[i]==1:
        count+=1

for i in range(1500,3000):
    if result[i]==0:
        count+=1

accuracy = float(count)/(len(result))
print accuracy