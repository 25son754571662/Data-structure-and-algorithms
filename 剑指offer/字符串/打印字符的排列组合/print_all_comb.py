class Solution:
    def Permutation(self, ss):
        if ss=='': return []
        n=len(ss)
        if n==1:return [ss]#只有一个字符，直接输出
        lst=[]
        #第1、2、...、n个字符在最前+递归剩下的情况
        for i in range(n):
            part1,part2=ss[0:i],ss[i+1:n]
            t=part1+part2
            lst+=[ss[i]+x for x in self.Permutation(t)]
        #去重复
        l=list(set(lst))
        l.sort(key=lst.index)
        return l