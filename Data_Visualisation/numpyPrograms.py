import numpy as np

arr = np.array([[1, 2, 3],[4, 9,5]])
print(arr)
print("shape:",arr.shape)
print("reshaped array:\n",arr.reshape(3,2))

print("multiplying with 0 :\n",arr*0)
print("multiplying with NaN :\n",arr*np.nan)
