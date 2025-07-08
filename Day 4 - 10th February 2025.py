# Numpy-4

import numpy as np
# Shallow Vs Deep Copy
a = np.arange(4)
print(a)
b = a.reshape(2, 2) # Shallow Copy - No change to original data
print(b)
a[0] = 100
print(a)
print(b) 
print(np.shares_memory(a, b))

a = np.arange(4)
print(a)
c = a + 2 # Deep Copy - Change to original data
print(c)
print(np.shares_memory(a, c))
a[0] = 100
print(a)
print(c)

a = np.arange(4)
d = a[::2] # Shallow Copy - No change to original data
print(a)
print(d)
d[0] = 1000
print(a)
print(d)
print(np.shares_memory(a, d))

a = np.arange(6)
print(a)
e = a[a%1 == 0] # Deep Copy - Change to original data
print(b)
a[0] = 100
print(a)
print(e)
print(np.shares_memory(a, e))

# view*() - To explicity mention shallow copy
a = np.arange(10)
a_shallow_copy = a.view()
print(np.shares_memory(a, a_shallow_copy))

a = np.arange(10)
b = a.view()
print(np.shares_memory(a,b))
b = b + 10
print(np.shares_memory(a,b))

# copy() - To explicity mention deep copy
b = np.arange(10)
b_deep_copy = b.copy()
print(np.shares_memory(b, b_deep_copy))

# Array Splitting


# split()
# hsplit()
# vsplit()

# Array Stacking
# hstack()
# vstack()
# concatenate()

