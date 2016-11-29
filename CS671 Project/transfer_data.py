import shutil
import random
import os

address = '/home/pratik/Desktop/maildir/data'
new_address = '/home/pratik/Desktop/maildir/red_data'

filenames = random.sample(os.listdir(address), 20000)
for fname in filenames:
    srcpath = os.path.join(address, fname)
    destpath =  os.path.join(new_address,fname)
    shutil.copyfile(srcpath, destpath)