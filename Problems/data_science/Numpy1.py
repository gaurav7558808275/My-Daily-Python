import numpy as np
qf = np.array([[1,2],[3,4],[5,6]],dtype=complex)
print(qf)
wq = np.array([[1,2],[3,4],[5,6]],ndmin =2)
print(wq)
print(np.shape(wq),np.shape(qf))
 
a = np.arange(36) #
print(a) 
print(wq.ndim) # returs the number of dimentations
print(a.reshape(6,1,6)) # convertes it into 3D

#item size returns the size of each elemet.
print()
print()
print(a.itemsize)