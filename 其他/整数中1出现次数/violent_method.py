class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        if n==1:return 1
        if n<=0:return 0
        sum=0
        for i in range(n):sum+=self.get_1(i+1)
        return sum
    def get_1(self,n):
        sum=1 if n%10==1 else 0
        while n/10 is not 0:
            n//=10
            if n%10==1:sum+=1
        return sum