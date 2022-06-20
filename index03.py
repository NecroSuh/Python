a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)
print(id(a))
print(id(b))

from copy import copy
c=[4,5,6]
d=copy(c)
c[2]=8
print(c)
print(d)
print(id(c))
print(id(d))
