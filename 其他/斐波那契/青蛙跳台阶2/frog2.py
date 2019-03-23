class Solution:
    def jumpFloorII(self, number):
        #不合法情况返回0，相当于没有跳法
        if number<=0:return 0
        #递归基为1
        if number==1:return 1
        #按第一步跳多少层来分类
        sum=1#第一步直接跳n层，有1种情况
        #第一步跳i层，有F(n-i)种情况，递归
        for i in [x+1 for x in range(number-1)]:
            sum+=self.jumpFloorII(number-i)
        return sum
		
class Solution:
    def jumpFloorII(self, number):
        return pow(2,number-1)