import sys
while True:
    n_temp=sys.stdin.readline().strip()
    if len(n_temp)==0:break
    n,nums=int(n_temp),[int(t) for t in input().split()]
    nums.sort()
    front,tail=0,n-1
    while(front+1<n and nums[front]==nums[front+1]):front+=1
    while(tail-1>=0 and nums[tail]==nums[tail-1]):tail-=1
    d_max=(front+1)*(n-tail)
 
    min_delta=nums[n-1]-nums[0]
    for i in range(n-1):
        d=nums[i+1]-nums[i]
        if d<min_delta:min_delta=d
 
    d_min=0
    p=0
    count=0
    while p<n-1:
        if nums[p]+min_delta==nums[p+1]:count+=1
        else:
            d_min+=count*(count+1)//2
            count=0
        p+=1
    d_min+=count*(count+1)//2
 
    print(d_min,d_max)