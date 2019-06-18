class Solution:
    def VerifySquenceOfBST(self, sequence):
        n=len(sequence)
        if n==0:return False
        if n<=2:return True
        last=sequence[n-1]#最后一个元素为根结点
        #看看左子树（如果有）是否合法
        p=n-2
        while p>=0:
            if sequence[p]<last:break
            p-=1
        if p>=0:#左子树居然有比根结点大的元素，返回False
            if max(sequence[0:p+1])>last:return False
            else:#左子树序列暂时合法，递归左子树
                if not self.VerifySquenceOfBST(sequence[0:p+1]):return False
        #递归右子树（如果有）是否合法
        last_2=sequence[n-2]#倒数第二位比根结点大，才有右子树
        if last_2>last:#有右子树，递归之
            if not self.VerifySquenceOfBST(sequence[p+1:n-1]):return False
        #所有情况都合法，返回True
        return True