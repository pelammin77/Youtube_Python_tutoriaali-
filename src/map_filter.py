#import math
#
# def laske_ympyran_ala(r):
#     return math.pi * (r ** 2)
#
#
#
# ympyran_sateet = [1.5, 3.0, 0.5, 5, 8, 1]
# #
# ympyran_alat = map(laske_ympyran_ala, ympyran_sateet)
# #
# print(ympyran_alat)
# #
# print(list(ympyran_alat))
# #
# print()
# print()


#
# ympyran_alat_lambda =  lambda r: math.pi *(r**2)
#
# print(list(map(ympyran_alat_lambda, ympyran_sateet)))
# #
#
# import statistics
# keskiarvot = [6, 6.5, 6.7, 7.2, 7.7, 8.2, 8.5, 8.7, 9, 9.2]
#
# avg = statistics.mean(keskiarvot)
#
# print(avg)
#
# print(list(filter(lambda x: x<avg, keskiarvot)))
# #
# #
# #
# nimet = ['Petri', '', 'Juha', '', 'Mika',0, 5 ]
#
# print (list(filter(None, nimet)))

#
from _functools import reduce

nums = list(range(1,11))

n = 1
for x in nums:
    n =  n*x

#
#
print(n)
#

multi = lambda x, y: x * y
print(reduce(multi, nums))
#
print(reduce(lambda x, y : x*y, nums))
