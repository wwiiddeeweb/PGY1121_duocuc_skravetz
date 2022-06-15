import numpy as np

arr1 = np.array([1,2,3,4,5,6,7,8,9], dtype=int)

print(arr1)
print(arr1[::-1])

indMax = np.where(arr1 == arr1.max())

print(arr1[indMax])
print("la suma: ", np.sum(arr1))

arr2 = arr1.copy()

print("promedio", arr2.mean())