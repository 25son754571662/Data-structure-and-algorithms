import sys
while True:
    s_temp=sys.stdin.readline().strip()
    if len(s_temp)==0:break
         
    s=[s_temp[t] for t in range(len(s_temp))]
    #交换法，类似于冒泡排序
    n,count=len(s),0
    while True:
        swap=False
        for i in range(n-1-count):
            if s[n-2-i]<'a' and s[n-1-i]>'Z':
                temp=s[n-2-i]
                s[n-2-i]=s[n-1-i]
                s[n-1-i]=temp
                i+=1
                swap=True
        count+=1
        if not swap:break
    S=''
    for i in range(n):S+=s[i]
    print(S)