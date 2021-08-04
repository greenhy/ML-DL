# List and Tuple
# List is mutable
# but Tuple is immutable

L = [7,[4,9,2],88]
# shallow copy and deep copy
import copy

Ls = L.copy()
Ld = copy.deepcopy(L)


#List extension
L1= [2*x-1 for x in (3,4,5,6)]
print(L1)
L2 = [2*x-y for x in (3,4,5,6) for y in range(4)]
print(L2)
L3 = [2*x-y for x in (3,4,5,6) for y in range(4) if abs(x-y)>2]
print(L3)

# type == Generator
G = (2*x-y for x in (3,4,5,6) for y in range(4) if abs(x-y)>2)
print(G)

print(dir(G))

# call generator related function
print(next(G))
print(next(G))
print(next(G))
print(next(G))

for v in G : print(v)

# generator function
# collatz sequence 
def genfun(n):
    while True:
        yield n # make n to generator
        if n%2 ==0:
            n = n/2
        else:
            n = 3*n+1
    # return is not needed


g = genfun(6)
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

import itertools
# all combinations of 3 elements
g = itertools.combinations('abcd',3)
for v in g:
    print(v)

print(list(g))
g = itertools.combinations('abcd',3)
print(list(g))