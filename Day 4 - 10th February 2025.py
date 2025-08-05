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
x1 = np.arange(9)
print(x1)
y1, y2, y3 = np.split(x1, 3) # Equi-Partitioning
print(y1, y2, y3)
z1, z2, z3 = np.split(x1, [2, 5]) # Non-Equi-Partitioning
print(z1, z2, z3)

# hsplit()
x2 = np.arange(16).reshape(4, 4)
print(x2)
y4, y5, y8 = np.hsplit(x2, [2, 3])
print(y4, y5, y8)
# vsplit()
x3 = np.arange(16).reshape(4, 4)
print(x3)
y6, y7 = np.vsplit(x3, 2)
print(y6, y7)
print(np.shape(x3), np.shape(y4))
y9, y10 = np.vsplit(x3, [2])

# Array Stacking
# hstack()
a1 = np.array([[1], [2], [3]])
a2 = np.array([[4], [5], [6]])
a3 = np.array([[7, 10], [8, 11], [9, 12]])
a_res = np.hstack((a1, a3, a2))
print(a_res)

# vstack()
b1 = np.array([[1, 2, 3], [10, 11, 12]])
b2 = np.array([4, 5, 6])
b3 = np.array([7, 8, 9])
b_res = np.vstack((b1, b3, b2))
print(b_res)
print(np.hstack((a1, a2)))

# concatenate()
c1 = np.array([[1, 2, 3], [10, 11, 12]])
c2 = np.array([[4, 5, 6]])
c_res = np.concatenate([c1, c2], axis=0)
print(c_res)
d1 = np.array([[1, 2, 3], [10, 11, 12]])
d2 = np.array([[4], [5]])
d_res = np.concatenate([d1, d2], axis=1)
print(d_res)



z = np.array([[1, 2, 3], [4, 5, 6]])
print(np.pad(z, 1, mode = 'constant', constant_values = 1))

arr = np.array([[1,2,3],
               [4,5,6],
               [7,8,9],
               [10,11,12]])
print(np.split(arr, 4))

arr = np.array([[[0, 1], 
             [2, 3]], 
 
            [[4, 5], 
             [6, 7]]])
print(arr[:, 0:,:1])

data = np.array([[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90],
                 [100, 110, 120]])

num_splits = 2
res = np.vsplit(data, num_splits)
print(res)
final = res[-1]
print(final)
print(np.vstack((final, np.vstack(res[:-1]))))
