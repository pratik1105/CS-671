import numpy as np
import matplotlib.pyplot as plt
from numpy import array

f=open('cosine_similarity.txt')
l1=f.read()
l2=l1.splitlines()

Value=array(l2)
Value=Value.astype(np.float)

plt.hist(Value,bins=10)
plt.title("Cosine Similarity")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()