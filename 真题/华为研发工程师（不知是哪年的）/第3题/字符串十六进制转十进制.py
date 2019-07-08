import sys
while True:
    s=sys.stdin.readline().strip()
    if len(s)==0:break
          
    l,n,num=s.split(),len(s)-2,0
    for i in range(n):
        num+=10+ord(s[i+2])-ord('A') if s[i+2]>='A' else int(s[i+2])
        if i<n-1:num*=16
    print(num)