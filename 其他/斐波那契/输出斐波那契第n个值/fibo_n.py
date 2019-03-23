def Fibonacci(n):
    if n == 0 or n == 1: return n
    # n>=2
    an_2 = 0
    an_1 = 1
    an = 0
    for i in range(n - 1):
        an = an_1 + an_2
        an_2=an_1
        n_1=an
    return an