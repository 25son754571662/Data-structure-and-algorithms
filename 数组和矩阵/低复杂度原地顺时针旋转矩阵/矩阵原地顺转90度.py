import numpy as np

n=5
arr=[[np.random.randint(10) for j in range(n)]for i in range(n)]

def rotate(arr):
    #按副对角线转置
    for i in range(n-1):
        for j in range(n-i-1):
            t=arr[i][j]
            arr[i][j]=arr[n-1-j][n-1-i]
            arr[n-1-j][n-1-i]=t
    #上下翻转
    for i in range(n//2):
        for j in range(n):
            t=arr[i][j]
            arr[i][j]=arr[n-i-1][j]
            arr[n-i-1][j]=t
    return
    
[print(arr[x]) for x in range(n)]
print('')
rotate(arr)
[print(arr[x]) for x in range(n)]