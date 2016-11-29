
import os
import glob
import shutil
import random
from os import listdir, chdir
import re
import shutil


maps={}
maps['Jan']=1
maps['Feb']=2
maps['Mar']=3
maps['Apr']=4
maps['May']=5
maps['Jun']=6
maps['Jul']=7
maps['Aug']=8
maps['Sep']=9
maps['Oct']=10
maps['Nov']=11
maps['Dec']=12

destaddress="/home/pratik/Desktop/Months"
chdir("/home/pratik/Desktop/maildir")
names = [d for d in listdir(".") if "." not in d]
for name in names:
    chdir("/home/pratik/Desktop/maildir/%s" % name)
    subfolders = listdir('.')
    sent_dirs = [n for n, sf in enumerate(subfolders) if "sent" in sf]
    sent_dirs_words = [subfolders[i] for i in sent_dirs]
    for d in sent_dirs_words:
        chdir('/home/pratik/Desktop/maildir/%s/%s' % (name,d))
        srcaddress=('/home/pratik/Desktop/maildir/%s/%s' % (name,d))
        file_list = listdir('.')
        for file in file_list:
        	if "." in file:
        		f=open(file,'r')
        		line=f.readline()
        		line=f.readline()
        		line=line.split(' ')
        		plholder=str(maps[line[3]])+'_'+line[4]
                srcpath=os.path.join(srcaddress, file)
                destpath=os.path.join(destaddress,plholder)
                destpath=os.path.join(destpath,file)
                shutil.copyfile(srcpath, destpath)