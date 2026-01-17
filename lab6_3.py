import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print("Element-wise:", a * b)
print("Iloczyn skalarny:", np.dot(a, b))
print("Iloczyn skalarny @:", a @ b)