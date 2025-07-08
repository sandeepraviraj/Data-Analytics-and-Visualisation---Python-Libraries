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

# Use-Case: Fitness Data Analysis

data = np.loadtxt('fit.txt', dtype = 'str')
#print(data)
print(data[0])
print(data[:5])

print(data[:, 0])
data_transpose = data.T
print(data_transpose)
date, step_count, mood, calories_burnt, hrs_of_sleep, status = data_transpose
print(date)
print(mood)
step_count = np.array(step_count, dtype = 'int')
calories_burnt = np.array(calories_burnt, dtype = 'int')
hrs_of_sleep = np.array(hrs_of_sleep, dtype = 'int')
print(step_count)
print(np.unique(mood, return_counts=True))
print(step_count.max())

happy_mood = step_count[mood == 'Happy']
print(len(happy_mood))
sad_mood = step_count[mood == 'Sad']
print(len(sad_mood))
neutral_mood = step_count[mood == 'Neutral']
print(len(neutral_mood))

happy_or_sad_mood = mood[(mood == 'Happy') | (mood == 'Sad')]
print(len(happy_or_sad_mood))

print(len(mood[mood == 'Happy']))
avg_step_count_happy = np.average(step_count[mood == 'Happy'])
print(avg_step_count_happy)
avg_step_count_sad = np.average(step_count[mood == 'Sad'])
print(avg_step_count_sad)

unique_mood = np.unique(mood[step_count > 4000], return_counts = True)
print(unique_mood)

