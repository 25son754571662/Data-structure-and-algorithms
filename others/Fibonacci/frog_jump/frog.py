class Solution:
    def jumpFloor(self, number):
        # write code here
        #跳一级：1种，#二级：1+1=2种 #三级：先1后2或先2后1，先2有2种，二级+一级共3种
        n=number
        if n==1 or n==2: return n
        an_2=1
        an_1=2
        an=0
        for i in range(n-2):
            an=an_2+an_1
            an_2=an_1
            an_1=an
        return an