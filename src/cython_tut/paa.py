# import python_esim
# import cython_esim
# res = cython_esim.test(10)
# print(res)
# res_2= python_esim.test(10)
# print(res_2)


import timeit
#
count = 10
cy_esim = timeit.timeit('cython_esim.test(10000)', setup='import cython_esim', number=count)
py_esim = timeit.timeit('python_esim.test(10000)', setup='import python_esim', number=count)



print(cy_esim, py_esim)
print("Cython on {} kertaa nopeampi".format(py_esim/cy_esim))

#res =cython_esim.test(100)

#print(res)