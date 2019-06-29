from numpy.random import rand

m,n=4,5

arr=[[0 for y in range(n)] for x in range(m)]

for i in range(m):
    for j in range(n):
        if i==0 and j==0:continue
        if i==m-1 and j==n-1:continue
        if rand()<0.2: arr[i][j]=1

#x、y为起点，m、n为arr大小
def all_valid_ways(arr,x,y):#直接把起点和终点交换都一样，还少些变量
    if arr[x][y]==1:return 0#障碍物位置算0种方案
    if x==0 and y==0:return 1#终点算1种方案
    if x==0 and not y==0:return all_valid_ways(arr,x,y-1)
    if y==0 and not x==0:return all_valid_ways(arr,x-1,y)
    return all_valid_ways(arr,x-1,y)+all_valid_ways(arr,x,y-1)
    
[print(arr[t]) for t in range(m)]    
print(all_valid_ways(arr,m-1,n-1))