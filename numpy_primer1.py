import numpy as np
import sys
import time

a = np.array([1,2,3])
print(a.size*a.itemsize)

b = np.array([(1,2,3),(4,5,6)])
print(a)
print(b)

l = [1,2,3]
print(sys.getsizeof(1)*len(l))

#numpy array takes less space
print("\n\nXXXXXXXXXXXXx")
for i,x in enumerate(l):
	print(i,x)

print("\n\nXXXXXXXXXXXXx")
for i in enumerate(l):
	print(i)

print("\n\nXXXXXXXXXXXXx")
l1 = range(5)
l2 = range(5)

result = [(x + y) for x,y in zip(l1,l2)]
print(result)
print("\n\nXXXXXXXXXXXXx")

n1 = np.arange(5)
n2 = np.arange(5)
result1 = n1 + n2
print (result1)

print("\n\nXXXXXXXXX Array dimension")
print(b.ndim)
print(b.dtype)
#print(b.itemSize)
print(b.size)
print(b.shape) #returns (row,col)

print("\n\nXXXXXXXXXXXXXXX")

#reshaping
a = np.array([(1,2,3,4),(3,4,5,6)]) #2x4
print(a)
a = a.reshape(4,2) # 4x2
print(a)

#slicing
print("\n\nXXXXXXXXXXXXXXX")
a = a.reshape(2,4)
print(a)
print(a[1,2])
print(a[:,1]) #all rows second element

