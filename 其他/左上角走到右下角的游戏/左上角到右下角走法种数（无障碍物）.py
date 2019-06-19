#m、n为矩阵行、列数
m,n=3,3

def all_ways(m,n):
    f=lambda p,q:fact(q)/fact(p)/fact(q-p)
    return f(m-1,m+n-2)

def fact(n):
    f=1
    for i in range(n):f*=(i+1)
    return f

print(all_ways(m,n))