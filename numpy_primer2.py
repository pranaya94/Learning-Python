import numpy as np 

a = np.linspace(1,3,8) #(start, end , number of nums) equally spaced
print(a)

print("\n",a.max())
print("\n",a.sum())

#axis ops
a = np.array([(1,2,3),
			 (4,5,6)])
print("\nSum of cols is ",a.sum(axis = 0)) #sum of columns
print("\nSum of cols is ",np.sum(a, axis = 0)) # same
print("\nSum of rows is ",a.sum(axis = 1))
print("\nSqrt of is ",np.sqrt(a))

#matrix ops

b = np.array([(1,2,3),(4,5,6)])
print(a + b) # in case of list it would have concatenated
print(a*b) #element wise

print("XXXXXXXXXXX")
print(a)
print(b)
print(np.vstack((a,b))) #vert stacking
print(np.hstack((a,b)))
print(a)
print("unrolled",a.ravel()) #unroll elements into 1D array

