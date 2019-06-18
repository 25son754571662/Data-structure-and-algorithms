class Solution:
    def NumberOf1(self, n):
        n_abs=abs(n)
        if n<0:return sum(self.to_buma(n))
        s=0
        while n_abs is not 0:
            s+=n_abs%2
            n_abs//=2
        return s
    #卧槽太脑残了，都没告诉你是按32位来算的
    def to_buma(self,origin_dec):
        l=[1]+[0 for x in range(31)]#符号位是1，其他位定0
        #特殊情况，直接返回
        if origin_dec==-pow(2,31):return l
        n=-origin_dec#转成正数（简称转正）
        count=0
        while n is not 0:
            l[32-count-1]=n%2
            n//=2
            count+=1
        #取反
        l[1:]=[1-x for x in l[1:]]
        #加一（包进位）
        inc=31
        while inc>=1:
            if l[inc]==0:
                l[inc]=1
                break
            else:
                l[inc]=0
                inc-=1
        return l