import sys
  
#肯定用递归
def fun(n):
    if n<=1:return 0
    if n==2:return 1
    x=n//3+fun(n//3+n%3)
    return x
  
while True:
    s=sys.stdin.readline().strip()
    if len(s)==0:break
    n=int(s)
    print(fun(n))