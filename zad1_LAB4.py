Moja_lista = [1, 17, 3, 5, 3, 4, 86, 90, 2, 21]
print(Moja_lista)

print(Moja_lista[0])
print(Moja_lista[-1])
print(len(Moja_lista))
print(max(Moja_lista))
print(min(Moja_lista))
print(sum(Moja_lista))
print(sorted(Moja_lista))

tmp = Moja_lista.copy()
tmp.append(6); print(tmp)
tmp.insert(2, 5); print(tmp)
popped = Moja_lista.pop(); print(popped)
tmp.reverse(); print(tmp)
combined = Moja_lista + [100,200]; print(combined)
repeated = [1,2]*3; print(repeated)

print(Moja_lista[:4], Moja_lista[3:], Moja_lista[::2], Moja_lista[::-1])