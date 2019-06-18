class Solution:
    def rectCover(self, number):
        n=number
        if n==1 or n==2: return n
        an_2=1
        an_1=2
        an=0
        for i in range(n-2):
            an=an_1+an_2
            an_2=an_1
            an_1=an
        return an