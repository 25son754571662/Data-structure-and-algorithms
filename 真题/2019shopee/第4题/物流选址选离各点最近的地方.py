n,M,sum_x,sum_y,count=int(input()),[],0,0,0
for i in range(n):M.append([int(t) for t in input().split()])
 
#找质心
for i in range(n):
    for j in range(n):
        if M[i][j]==1:
            sum_x+=i
            sum_y+=j
            count+=1
#质心坐标(<=0.5舍>0.5入)
x_mean,y_mean=sum_x//count+(1 if sum_x/count>0.5 else 0),sum_y//count+(1 if sum_y/count>0.5 else 0)
 
def d(M,x,y,n):#求一个点到其他点的距离
    sum_d_x,sum_d_y,count=0,0,0
    for i in range(n):
        for j in range(n):
            if M[i][j]==1:
                sum_d_x+=abs(x-i)
                sum_d_y+=abs(y-j)
    return sum_d_x+sum_d_y
             
#依次找离质心的距离为1、2、...的点
#先计算所有点到质心的距离
D_to_center=[[abs(i-x_mean)+abs(j-y_mean) for j in range(n)] for i in range(n)]
#归纳出到质心距离为1、、2、...的点坐标
l=[[] for t in range(2*n-2)]#距离最大可能为2n-2
for i in range(n):
    for j in range(n):l[D_to_center[i][j]].append([i,j])
 
d_min=-1
if M[x_mean][y_mean]==0: #质心及其周围8个点
    for i in range(3):
        for j in range(3):
            if M[x_mean+i-1][y_mean+j-1]==0:
                D=d(M,x_mean+i-1,y_mean+j-1,n)
                if D<d_min or d_min==-1:d_min=D
else:#质心附近其他点
    for l_i in l:
        flag=False
        for p in l_i:
            if M[p[0]][p[1]]==0:
                D=d(M,p[0],p[1],n)#该点到其他点的距离
                if D<d_min or d_min==-1:d_min=D
                flag=True
        if flag:break
         
print(d_min)