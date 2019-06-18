class Solution:
    def Power(self, a, e):
        # write code here
        flag=True
        if e<0: 
            e=-e
            flag=False
        if e == 1: return a
        if e==0: return 1
        e_ = int(e / 2)
        t = Solution.Power(self,a, e_)
        result_temp=t * t if e % 2 == 0 else t * t * a
        return result_temp if flag else 1/result_temp