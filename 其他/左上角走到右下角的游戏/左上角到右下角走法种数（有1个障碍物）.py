import numpy as np

#m、n为矩阵行、列数，x、y为障碍物坐标（0开始）
m,n,x,y=3,3,0,1

def all_valid_ways(m,n,x,y):
    f=lambda p,q:fact(q)/fact(p)/fact(q-p)
    return f(m-1,m+n-2)-f(x,x+y)*f(m-x-1,m-x+n-y-2)

def fact(n):
    f=1
    for i in range(n):f*=(i+1)
    return f

arr=[[0 for v in range(n)]for u in range(m)]
arr[x][y]=1
[print(arr[t]) for t in range(m)]
print(all_valid_ways(m,n,x,y))