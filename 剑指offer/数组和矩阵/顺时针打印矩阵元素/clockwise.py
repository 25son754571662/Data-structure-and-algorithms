import numpy as np
def cycle(arr):
    n=np.size(arr,0)
    if n==0:return []
    if n==1:return [arr[0,0]]
    lst=[x for x in arr[0,:]]
    lst+=[x for x in arr[1:n,n-1]]
    temp1=[x for x in arr[n-1,0:n-1]]
    temp1.reverse()
    temp2=[x for x in arr[1:n-1,0]]
    temp2.reverse()
    lst+=temp1
    lst+=temp2
    lst+=cycle(arr[1:n-1,1:n-1])
    return lst
#n x n
n=7
arr=np.zeros([n,n])
arr=arr.astype(np.int)
for i in range(n):
    for j in range(n):arr[i,j]=n*i+j+1
print(arr)
print(cycle(arr))