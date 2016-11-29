import numpy as np
import matplotlib.pyplot as plt
from os import listdir, chdir

chdir('/home/pratik/Desktop/NewMonths')
names = [d for d in listdir(".") if "." not in d]

arr1=[]
arr2=[]
arr3=[]
arr4=[]

for name in sorted(names):
	#print(name+'\n')
	chdir('/home/pratik/Desktop/NewMonths/%s' %name)
	f=open('info.txt','r')
	arr1.append(float(f.readline()))
	arr2.append(float(f.readline()))
	arr3.append(float(f.readline()))
	arr4.append(float(f.readline()))
	f.close()

arr1=np.array(arr1)
arr2=np.array(arr2)
arr3=np.array(arr3)
arr4=np.array(arr4)

plt.plot(arr1)
plt.show()
plt.plot(arr2)
plt.show()
plt.plot(arr3)
plt.show()
plt.plot(arr4)
plt.show()