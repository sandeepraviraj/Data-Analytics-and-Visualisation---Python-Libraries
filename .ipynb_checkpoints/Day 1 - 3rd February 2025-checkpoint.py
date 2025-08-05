# Numpy-1

# Python List Vs Numpy Array
# Numpy Array - They are homogeneous.
import numpy as np
a = np.array([1, 2, 3, 4, 5]) # Converts List to Array
print(a)
res = a ** 2
print(res)

b = np.array(list(range(1000000)))
res = b ** 2
print(b)
print(res)
print(b.ndim) # Displays the Dimension Of The Array
print(b.shape) # Displays the count of columns and rowa in the array(colmn, row)

c = np.arange(1, 5, 0.5) # Float step-size can be performed
print(c)

d = np.arange(5)
print(d)
d[2:4] = 0
print(d)
print(d[0:2])

# Type Conversion
e = np.array([1, 2, 3, 4.5, 5]) # Numpy Arrays converts the data automatically to maintai homgenity across all values. Here All the integers are converted into float.
print(e)

f = np.array([1, 2, 3, '4.5', 5, 6.5], dtype = 'float')
print(f)

g = np.array([1, 2, 3, '4.5', 5, 6.5])
g = g.astype('float')
print(g)

# Indexing & Slicing
h = np.arange(1, 13)
print(h)
print(h[0])
print(h[-1])
print(h[[-1, -2, -3, 1, 2, 3]]) # Accepts list of arrays

print(h[:5])
print(h[-5:-1])
print(h[-5:-1:-1])
print(h[6:])
print(h < 6)
print(h[h < 6])
print(h[h % 2 == 0])

m1 = np.array([1, 2, 3, 4, 5])
m2 = np.array([8, 7, 6])
m1[2:] = m2[::-1]
print(m1)

# Use-Case: Net Promoters Score(NPS)
