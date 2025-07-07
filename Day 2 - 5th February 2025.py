# Numpy-2

# 2-D Arrays

import numpy as np
a = np.array(range(16))
print(a)
print(len(a))
print(a.shape)
print(a.ndim)

b = a.reshape(4,4) # Used to conver 1-D Array to 2-D Array
print(b)
print(len(b))
print(b.ndim)
print(b.shape)
print(b.T) # To Transpose a 2-D Array
print(a.reshape(8, -1)) # -1 is used to automatically calculate the number of columns

# Indexing and Slicing

print(b[2, 2])
print(b[2][2])
print(b[2, : 2])
print(b[:, 2])
print(b[[0, 1, 2, 3], [0, 1, 2, 3]])
print(b[:2])
print(b[:, 1:3])
print(b[b % 2 ==0])

# Aggregate Functions
c = np.array(range(1, 10))
print(c)
print(np.sum(c))
print(np.min(c))
print(np.max(c))
print(np.average(c))

d = c.reshape(3,3)
print(d)
print(np.sum(d))
print(np.sum(d, axis=0))
print(np.sum(d, axis=1))

# Logical Operations
prices = np.array([35, 45, 20, 25, 50])
budget = 30
can_afford = np.any(prices <= budget)
print(can_afford)

can_afford_all = np.all(prices <= budget)
print(can_afford_all)
print(prices[prices > budget])

k1 = np.array([1, 2, 0, 2])
k2 = np.array([2, 2, 3, 6])
k3 = np.array([6, 4, 4, 5])

print(((k1 <= k2) & (k2 <= k3)).any())
print(((k1 <= k2) & (k2 <= k3)).all())

original_prices = np.array([35, 45, 20, 25, 50]) 
discount_prices = np.where(original_prices > 35, original_prices * 0.65, original_prices)

print(discount_prices)

print(np.where(k1))
print(np.asarray(k1).nonzero())

# Use-Case: Fitness Data