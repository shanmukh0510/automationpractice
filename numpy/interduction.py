#numpy is a linbrary is used to work with arrys
#It also has functions for working in domain of linear algebra, fourier transform, and matrices
#NumPy stands for Numerical Python

# In Python we have lists that serve the purpose of arrays, but they are slow to process.

# NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

import  numpy as np

arr = np.array([1,3,56,76,99,36])
print(arr)

"""
Array Operations
Vectorized computations (no loops!)
"""
print(arr +5)

#3. Array Slicing and Indexing

print(arr[::-1])

#Random Number Generation

print(np.random.randint(1,100,size = 5))
