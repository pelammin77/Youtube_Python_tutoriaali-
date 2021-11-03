cpdef  test(r):
    cdef int x=0
    cdef int i=0
    for i in range(r):
        x+= i
    return x


