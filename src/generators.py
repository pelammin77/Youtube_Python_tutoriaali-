import sys

MAX = 101


def luo_neliot_lista(n):
    neliot = [i ** 2 for i in range(1, n)]
    return neliot

neliot = luo_neliot_lista(MAX)

print(neliot)
print(sys.getsizeof(neliot))



def gen(n):
    for i in range(1,n):
        yield i**2


#
g = gen(MAX)
# print(g)
#
# print(next(g))
# print(next(g))



for n in g:
    print(n)
print(sys.getsizeof(g))

