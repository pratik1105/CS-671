from os import chdir,listdir
import re
import os

chdir("/home/pratik/Desktop/nlp/Brown-data/test")
names = [d for d in listdir(".") if "." not in d]

chdir("/home/pratik/Desktop/nlp/Brown-data/Correct")

new_names=[d for d in listdir(".") if "." not in d]

for word in new_names:
	if word not in names:
		os.remove('%s' %(word))