f=lambda t:int(t)
[x,y,n]= [f(x) for x in input().split()]

m=[[0 for i in range(y+1)]for j in range(x+1)]
for i in range(n):
    temp=input().split()
    m[f(temp[0])][f(temp[1])]=1
    
'''此方法超时（暴力递归）
def myfun(m,x,y):#直接把起点和终点交换吧，都一样，还少些变量
    if m[x][y]==1:return 0#怪物位置算0种方案
    if x==0 or y==0:return 1#到边缘算1种方案
    return myfun(m,x-1,y)+myfun(m,x,y-1)
'''

'''有效走法=所有走法-不可行走法（也是递归）'''
def myfun(m,x,y,x0,y0):#所有走法，有C(x-x0，x+y-x0-y0)种
    f=lambda n:1 if n==0 else n*f(n-1)
    C=lambda m,n:f(n)//(f(m)*f(n-m))
    all_ways,invalid_ways=C(x-x0,x+y-x0-y0),0
    for i in range(x-x0+1):#从右往左，从下往上扫描，找候选boss
        for j in range(y-y0+1):
            p,q=x-i,j+y0
            if (p==x0 and q==y0)or (p==x and q==x):continue
            if m[p][q]==1:invalid_ways+=myfun(m,x,y,p,q)*C(p-x0,p+q-x0-y0)
    return all_ways-invalid_ways

print(myfun(m,x,y,0,0))