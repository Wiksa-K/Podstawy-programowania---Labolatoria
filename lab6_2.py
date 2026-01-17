import numpy as np

rng = np.random.default_rng(42)
M = rng.normal(0, 1, size=(6, 4))
print(M)

mean_col = M.mean(axis=0)
print("Średnia kolumn:", mean_col)

min_ind = M.argmin(axis=0)
max_ind = M.argmax(axis=0)

print("Indeksy min:", min_ind)
print("Indeksy max:", max_ind)