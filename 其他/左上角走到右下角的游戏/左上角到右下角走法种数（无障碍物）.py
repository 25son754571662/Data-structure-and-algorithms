#m、n为矩阵行、列数
m,n=4,4

def all_ways(m,n):
    f=lambda n:1 if n==0 else n*f(n-1)
    C=lambda p,q:f(q)/f(p)/f(q-p)
    return C(m-1,m+n-2)

print(all_ways(m,n))