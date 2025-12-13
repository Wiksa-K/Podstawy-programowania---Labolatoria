def t(x, *, y, z=0):
 return x + y + z
val= t(1, 2, z=3)

f = lambda a, /, *args, b=0: (a, sum(args) + b)
y = f(3, 4, 5, b=2)