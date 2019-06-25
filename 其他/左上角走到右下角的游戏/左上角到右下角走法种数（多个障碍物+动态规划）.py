f=lambda t:int(t)
[x,y,n]= [f(x) for x in input().split()]

m=[[1 for i in range(y+1)]for j in range(x+1)]
for i in range(n):
    temp=input().split()
    m[f(temp[0])][f(temp[1])]=0
    
def myfun(m,x,y):
    for i in range(x+1):
        for j in range(y+1):
            if m[i][j]==0 or (i==0 and j==0):continue
            m[i][j]=(0 if i==0 else m[i-1][j])+(0 if j==0 else m[i][j-1])
    return m[x][y]
	
print(myfun(m,x,y))