import sys
import time

def gera():
    r = []
    for n in range(100):
        r.append(n)
        time.sleep(0.1)
    return r

g = gera()

print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))

for v in g:
    print(v)


# lista = list(range(10))
#
# print(sys.getsizeof(lista))


# lista = [0,1,2,3,4,5]
# lista = iter(lista)
#
# print(next(lista))
#
# print(hasattr(lista, '__next__'))

# for v in lista:
#     print(v)
#
# lista = 'String'

# print(hasattr(lista, '__iter__'))


# import sys
# import time
#
# l1 = [x for x in range(100000)]
# l2 = (x for x in range(100000))
#
# for v in l2:
#     print(v)