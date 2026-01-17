import numpy as np

A = np.arange(25).reshape(5, 5)
print(A)

top = A[0, :]
bottom = A[-1, :]
left = A[:, 0]
right = A[:, -1]

print("Góra:", top)
print("Dół:", bottom)
print("Lewo:", left)
print("Prawo", right)