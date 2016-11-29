from os import chdir,listdir
import re
import os

chdir("/home/pratik/Desktop/nlp/Brown-data/test/")
names = [d for d in listdir(".") if "." not in d]
names.remove('ce10~')

chdir("/home/pratik/Desktop/nlp/Brown-data/train/")
for name in names:
	os.remove('%s' %(name))