from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
from gensim import corpora, models
import gensim
import os
import glob
import shutil
import random
from os import listdir, chdir
import re
import shutil

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')
extendedstopwords=["pst","hou","ect","0f","re","ve","please","time","pm","am","cc","www","http","com","ll","a","about","above","across","after","MIME Version","forwarded","again","against","all","almost","alone","along","already","also","although","always","am","among","an","and","another","any","anybody","anyone","anything","anywhere","are","area","areas","aren't","around","as","ask","asked","asking","asks","at","away","b","back","backed","backing","backs","be","became","because","become","becomes","been","before","began","behind","being","beings","below","best","better","between","big","both","but","by","c","came","can","cannot","can't","case","cases","certain","certainly","clear","clearly","come","could","couldn't","d","did","didn't","differ","different","differently","do","does","doesn't","doing","done","don't","down","downed","downing","downs","during","e","each","early","either","end","ended","ending","ends","enough","even","evenly","ever","every","everybody","everyone","everything","everywhere","f","face","faces","fact","facts","far","felt","few","find","finds","first","for","four","from","full","fully","further","furthered","furthering","furthers","g","gave","general","generally","get","gets","give","given","gives","go","going","good","goods","got","great","greater","greatest","group","grouped","grouping","groups","h","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","her","here","here's","hers","herself","he's","high","higher","highest","him","himself","his","how","however","how's","i","i'd","if","i'll","i'm","important","in","interest","interested","interesting","interests","into","is","isn't","it","its","it's","itself","i've","j","just","k","keep","keeps","kind","knew","know","known","knows","l","large","largely","last","later","latest","least","less","let","lets","let's","like","likely","long","longer","longest","m","made","make","making","man","many","may","me","member","members","men","might","more","most","mostly","mr","mrs","much","must","mustn't","my","myself","n","necessary","need","needed","needing","needs","never","new","newer","newest","next","no","nobody","non","noone","nor","not","nothing","now","nowhere","number","numbers","o","of","off","often","old","older","oldest","on","once","one","only","open","opened","opening","opens","or","order","ordered","ordering","orders","other","others","ought","our","ours","ourselves","out","over","own","p","part","parted","parting","parts","per","perhaps","place","places","point","pointed","pointing","points","possible","present","presented","presenting","presents","problem","problems","put","puts","q","quite","r","rather","really","right","room","rooms","s","said","same","saw","say","says","second","seconds","see","seem","seemed","seeming","seems","sees","several","shall","shan't","she","she'd","she'll","she's","should","shouldn't","show","showed","showing","shows","side","sides","since","small","smaller","smallest","so","some","somebody","someone","something","somewhere","state","states","still","such","sure","t","take","taken","than","that","that's","the","their","theirs","them","themselves","then","there","therefore","there's","these","they","they'd","they'll","they're","they've","thing","things","think","thinks","this","those","though","thought","thoughts","three","through","thus","to","today","together","too","took","toward","turn","turned","turning","turns","two","u","under","until","up","upon","us","use","used","uses","v","very","w","want","wanted","wanting","wants","was","wasn't","way","ways","we","we'd","well","we'll","wells","went","were","we're","weren't","we've","what","what's","when","when's","where","where's","whether","which","while","who","whole","whom","who's","whose","why","why's","will","with","within","without","won't","work","worked","working","works","would","wouldn't","x","y","year","years","yes","yet","you","you'd","you'll","young","younger","youngest","your","you're","yours","yourself","yourselves","you've","'ve","z"]
en_stop.extend(extendedstopwords)
# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
list1=['enron','thanks','agreement','corp','deal','attached','doc','contract','gas','fax','information','mail','intended','file','sent','message','kay','call','review','north']
list2=['thanks','call','don','week','meeting','mail','day','enron','message','hope','houston','home','vince','love','night','friday','thursday','tomorrow','talk','weekend']
list3=['enron','power','energy','market','company','business','california','gas','risk','vince','jeff','trading','management','information','price','meeting','markets','financial','news','prices']
list4=['thanks','dec','mid','net','columbia','john','meeting','gas','tw','gif','report','david','images','project','mark','system','m0','asp','scott','rick']

chdir('/home/pratik/Desktop/NewMonths')
names = [d for d in listdir(".") if "." not in d]
for name in names:
	chdir("/home/pratik/Desktop/NewMonths/%s" % name)
	count1=0
	count2=0
	count3=0
	count4=0
	file_list = listdir('.')
	for file in file_list:
		if "." in file:
			f=open(file,'r')
			inp = f.read().replace('\n','')
			raw = inp.lower()
			tokens = tokenizer.tokenize(raw)
			stopped_tokens = [i for i in tokens if not i in en_stop]
			no_integers = [x for x in stopped_tokens if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
			for word in no_integers:
				if word in list1:
					count1+=1
				if word in list2:
					count2+=1
				if word in list3:
					count3+=1
				if word in list4:
					count4+=1
	f=open('info.txt','w')
	f.write(str(count1)+'\n')
	f.write(str(count2)+'\n')
	f.write(str(count3)+'\n')
	f.write(str(count4)+'\n')
	f.close()