from numpy.random import rand

m,n=4,5

arr=[[0 for x in range(n)] for y in range(m)]

for i in range(m):
    for j in range(n):
        if i==0 and j==0:continue
        if i==m-1 and j==n-1:continue
        if rand()<0.2: arr[i][j]=1

#x、y为起点，m、n为arr大小
def all_valid_ways(arr,x,y,m,n):
    if arr[x][y]==1:return 0#如果是障碍物块
    if x==m-1 and y==n-1:return 1#到终点算1种方法
    if x==m-1:return all_valid_ways(arr,x,y+1,m,n)#行走到底了
    if y==n-1:return all_valid_ways(arr,x+1,y,m,n)#列走到底了
    return all_valid_ways(arr,x+1,y,m,n)+all_valid_ways(arr,x,y+1,m,n)
    
[print(arr[t]) for t in range(m)]    
print(all_valid_ways(arr,0,0,m,n))