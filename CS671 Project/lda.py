from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os
import glob
import shutil
import random
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')
extendedstopwords=["pst","hou","ect","0f","re","ve","please","time","pm","am","cc","www","http","com","ll","a","about","above","across","after","MIME Version","forwarded","again","against","all","almost","alone","along","already","also","although","always","am","among","an","and","another","any","anybody","anyone","anything","anywhere","are","area","areas","aren't","around","as","ask","asked","asking","asks","at","away","b","back","backed","backing","backs","be","became","because","become","becomes","been","before","began","behind","being","beings","below","best","better","between","big","both","but","by","c","came","can","cannot","can't","case","cases","certain","certainly","clear","clearly","come","could","couldn't","d","did","didn't","differ","different","differently","do","does","doesn't","doing","done","don't","down","downed","downing","downs","during","e","each","early","either","end","ended","ending","ends","enough","even","evenly","ever","every","everybody","everyone","everything","everywhere","f","face","faces","fact","facts","far","felt","few","find","finds","first","for","four","from","full","fully","further","furthered","furthering","furthers","g","gave","general","generally","get","gets","give","given","gives","go","going","good","goods","got","great","greater","greatest","group","grouped","grouping","groups","h","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","her","here","here's","hers","herself","he's","high","higher","highest","him","himself","his","how","however","how's","i","i'd","if","i'll","i'm","important","in","interest","interested","interesting","interests","into","is","isn't","it","its","it's","itself","i've","j","just","k","keep","keeps","kind","knew","know","known","knows","l","large","largely","last","later","latest","least","less","let","lets","let's","like","likely","long","longer","longest","m","made","make","making","man","many","may","me","member","members","men","might","more","most","mostly","mr","mrs","much","must","mustn't","my","myself","n","necessary","need","needed","needing","needs","never","new","newer","newest","next","no","nobody","non","noone","nor","not","nothing","now","nowhere","number","numbers","o","of","off","often","old","older","oldest","on","once","one","only","open","opened","opening","opens","or","order","ordered","ordering","orders","other","others","ought","our","ours","ourselves","out","over","own","p","part","parted","parting","parts","per","perhaps","place","places","point","pointed","pointing","points","possible","present","presented","presenting","presents","problem","problems","put","puts","q","quite","r","rather","really","right","room","rooms","s","said","same","saw","say","says","second","seconds","see","seem","seemed","seeming","seems","sees","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","show","showed","showing","shows","side","sides","since","small","smaller","smallest","so","some","somebody","someone","something","somewhere","state","states","still","such","sure","t","take","taken","than","that","that's","the","their","theirs","them","themselves","then","there","therefore","there's","these","they","they'd","they'll","they're","they've","thing","things","think","thinks","this","those","though","thought","thoughts","three","through","thus","to","today","together","too","took","toward","turn","turned","turning","turns","two","u","under","until","up","upon","us","use","used","uses","v","very","w","want","wanted","wanting","wants","was","wasn't","way","ways","we","we'd","well","we'll","wells","went","were","we're","weren't","we've","what","what's","when","when's","where","where's","whether","which","while","who","whole","whom","who's","whose","why","why's","will","with","within","without","won't","work","worked","working","works","would","wouldn't","x","y","year","years","yes","yet","you","you'd","you'll","young","younger","youngest","your","you're","yours","yourself","yourselves","you've","'ve","z"]
en_stop.extend(extendedstopwords)
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents
#doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
#doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
#doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
#doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
#doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list
address = '/home/pratik/Desktop/maildir/data/'
new_address = '/home/pratik/Desktop/maildir/red_data'
doc_set=[]

path = '/home/pratik/Desktop/maildir/red_data/*.txt'   
files=glob.glob(path)   
for file in files:     
    f=open(file, 'r')  
    str = f.read().replace('\n','')   
    doc_set.append(str)

# list for tokenized documents in loop
texts = []



# loop through document list
for i in doc_set:
    
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    #for p in tokens:
    #	print(p)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    no_integers = [x for x in stopped_tokens if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
    # stem tokens
    #stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    
    # add tokens to list
    texts.append(no_integers)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', 
    level=logging.INFO)

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=4, id2word = dictionary, passes=2)
topics=ldamodel.show_topics(num_topics=4, num_words=20,formatted=False)
f=open("topics.txt",'w')
for tples in topics:
    b=tples[1]
    for tups in b:
        f.write(tups[0]+"\n")

    f.write("\n\n\n\n\n\n\n\n")
