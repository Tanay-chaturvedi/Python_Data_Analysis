# n=[1,2,3]
# res=[]
# for _ in n:
#     res.append(_+5)
# print(res)

import numpy as np
# n=[1,2,3]
# arr=np.array(n)
# print(arr+5)


# No loop!
# NumPy performs the operation on the entire array.
# This is called Vectorization.

arr = np.array([5,10,15,20,25])
print(arr[0])
print(arr[-1])
print(arr.shape)
print(arr.size)
print(arr.dtype)
print(arr[2:])
print(arr[::-1])