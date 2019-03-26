class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<=0:return
        i,t=0,1
        while True:
            r=t
            while True:
                mode=[r%2,r%5,r%3]
                if mode[0]==0:r/=2
                if mode[1]==0:r/=5
                if mode[2]==0:r/=3
                mode_condition=int(mode[0]*mode[1]*mode[2]) is not 0
                if r==1 or mode_condition:break
            if r==1:i+=1
            if i==index: return t
            t+=1