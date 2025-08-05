# Numpy-3
import numpy as np

# Sorting
a = np.array([4, 7, 0, 3, 8, 2, 5, 1, 6, 9])
print(a)
b = np.sort(a) # Ascending Sorting
print(b)
c = np.sort(a)[::-1] # Descending Sorting
print(c)
d = np.array([[1, 5, 3], [2, 9, 6], [7, 4, 8]])
print(d)
e = np.sort(d) # Ascending Sorting row-wise
print(e)
f = np.sort(d, axis=0)# Ascending Sorting column-wise
print(f)
g = np.sort(d)[::,::-1]# Descending Sorting row-wise
print(g)
h = np.sort(d, axis=0)[::-1] # Descending Sorting column-wise
print(h)


# Element-Wise Multiplication
a1 = np.arange(1, 6)
print(a1)
b1 = np.arange(6, 11)
print(b1)
print(a1 * b1)
c1 = np.array([1, 2, 3])
print(c1)
# print(a1 * c1) --> ValueError: operands could not be broadcast together with shapes (5,) (3,)

a2 = np.arange(6, 15).reshape(3, 3)
print(a2)
b2 = np.arange(15, 24).reshape(3, 3)
print(b2)
print(a2 * b2)
c2 = np.array([[1, 2, 3], [4, 5, 6]])
# print(a2 * c2) --> ValueError: operands could not be broadcast together with shapes (3,3) (2,3)

# Matrix Multiplication --> np.dot or (np.matmul/ @)
# Matrix Multiplication is possible if c1 = r2
a3 = np.arange(1, 5).reshape(2, 2)
print(a3)
b3 = np.arange(6, 12).reshape(2, 3)
print(b3)
print(np.dot(a3, b3))
print(a3 @ b3)
print(np.matmul(a3, b3))

# Vectorization
a4 = np.arange(10)
print(a4)
print(np.where(a4 % 2 == 0, a4 + 2, a4 - 2))

def even_odd(arr):
    if np.any(arr % 2 == 0):
        arr += 2
    else:
        arr -= 2
    return arr

res = np.vectorize(even_odd)(a4) # np.vectorize() ---> Accepts array as a parameter to perform the operation.
print(res)

# Broadcasting
print("Broadcasting")
print(np.tile(np.arange(0, 40, 10), (3, 1)))
a5 = np.tile(np.arange(0, 40, 10), (3, 1)).T
print(a5)
b5 = np.tile(np.arange(0, 3), (4, 1))
print(b5)
print(a5 + b5)
c5 = np.arange(0, 3)
print(c5)
print(a5 + c5)
d5 = np.arange(0, 40, 10).reshape(4, 1)
print(d5)
print(c5 + d5)
print(a5.ndim)
print(b5.ndim)
print(c5.ndim)
print(d5.ndim)

x = np.array([1, 2, 3])
y = np.array([[4, 5, 6]])
print(x.ndim)
print(y.ndim)
print(x.shape)
print(y.shape)


arr1 = np.array([[1,2], [3,4]])
arr2 = np.array([1,1])
print(arr1)
print(arr2)
print(np.dot(arr1, arr2))


birds = np.array(['macaw', 'owl', 'parrot', 'macaw', 'peacock', 'owl', 'macaw', 'sparrow', 'macaw', 'parrot', 'sparrow', 'parrot', 'owl', 'owl', 'macaw'])
age = np.array([8, 7, 4, 13, 11, 13, 3, 11, 14, 8, 4, 1, 3, 10, 1])
max_age = np.max(age)
print(age[max_age])
old_bird = birds[age == np.max(age)][0]
print(old_bird)


