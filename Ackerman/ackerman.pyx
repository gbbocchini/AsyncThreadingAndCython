import cython


cpdef int ack(m: cython.int = 0, n: cython.int = 0):
    if m == 0:
        return n+1
    if n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1, ack(m,n-1))
