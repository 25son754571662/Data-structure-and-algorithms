import sys
while True:
    #读第一行
    try_read=sys.stdin.readline().strip()
    if len(try_read)==0:break
    N,M=[int(t) for t in try_read.split()]
    #读第二行
    scores=[int(t) for t in input().split()]
    #读M个操作
    for i in range(M):
        s_temp=input().split()
        s=[s_temp[i] if i==0 else int(s_temp[i]) for i in range(3)]
        #先完成，再考虑效率
        if s[0]=='Q':
            max_score=0
            p=s[2]>s[1]
            d=s[2]-s[1] if p else s[1]-s[2]
            start=s[1] if p else s[2]
            for x in [start+t-1 for t in range(d+1)]:
                if scores[x]>max_score:max_score=scores[x]
            print(max_score)
        if s[0]=='U':scores[s[1]-1]=s[2]