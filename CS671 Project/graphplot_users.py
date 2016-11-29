import numpy as np
import matplotlib.pyplot as plt
from os import listdir, chdir
import sys
chdir('/home/pratik/Desktop/NewUsers')
names = [d for d in listdir(".") if "." not in d]


for name in names:
	chdir('/home/pratik/Desktop/NewUsers/%s' % name)
	arr1=[]
	arr2=[]
	arr3=[]
	arr4=[]
	newnames=[d for d in listdir(".") if "." not in d]
	for newname in sorted(newnames):
		chdir('/home/pratik/Desktop/NewUsers/%s/%s' % (name,newname))
		f=open('info.txt','r')
		arr1.append(int(f.readline()))
		arr2.append(int(f.readline()))
		arr3.append(int(f.readline()))
		arr4.append(int(f.readline()))
		f.close()

	chdir('/home/pratik/Desktop/NewUsers/%s' % name)
	arr1=np.array(arr1)
	arr2=np.array(arr2)
	arr3=np.array(arr3)
	arr4=np.array(arr4)

	plt.plot(arr1)
	plt.savefig('%s_fig1.png' %(name),bbox_inches='tight')
	plt.gcf().clear()

	plt.plot(arr2)
	plt.title('"meetings" versus time')
	plt.xlabel('time(in months)')
	plt.ylabel('frequency')
	plt.savefig('%s_fig2.png' %(name),bbox_inches='tight')
	plt.gcf().clear()
	
	plt.plot(arr3,color='red')
	plt.title('"business" versus time')
	plt.xlabel('time(in months)')
	plt.ylabel('frequency')
	plt.savefig('%s_fig3.png' %(name),bbox_inches='tight')
	plt.gcf().clear()
	
	plt.plot(arr4)
	plt.savefig('%s_fig4.png' %(name),bbox_inches='tight')
	plt.gcf().clear()
	