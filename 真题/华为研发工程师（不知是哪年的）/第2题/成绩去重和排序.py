import sys
while True:
    n,s=0,[]
    s_temp=sys.stdin.readline().strip()
    if len(s_temp)==0:break
    n=int(s_temp)
    for i in range(n):s.append(int(sys.stdin.readline().strip()))
    s.sort()
 
    for i in range(n-1):
        #从后到前，复杂度低一点
        if s[n-1-i]==s[n-i-2]:
            s.pop(n-1-i)
 
    [print(s[j]) for j in range(len(s))]