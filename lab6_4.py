import numpy as np

A = np.arange(6).reshape(2, 3)
B = np.arange(6).reshape(3, 2)

print(A @ B)
print(B @ A)

B2 = np.arange(9).reshape(3, 3)

print(A @ B2)