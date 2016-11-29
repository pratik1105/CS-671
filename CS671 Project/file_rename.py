from os import listdir, chdir
import sys
import os

chdir('/home/pratik/Desktop/NewMonths')
for filename in os.listdir('.'):
	a,b=filename.split('_')
		
	if a=='1':
		a='01'
	elif a=='2':
		a='02'
	elif a=='3':
		a='03'
	elif a=='4':
		a='04'
	elif a=='5':
		a='05'
	elif a=='6':
		a='06'
	elif a=='7':
		a='07'
	elif a=='8':
		a='08'
	elif a=='9':
		a='09'

	newfilename=b+'_'+a
	print filename
	os.rename(filename,newfilename)
