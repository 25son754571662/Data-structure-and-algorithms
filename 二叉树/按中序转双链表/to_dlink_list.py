class Solution:
    def Convert(self, pRootOfTree):
        if pRootOfTree==None:return None
        #思路：用一个list，目标顺序是中序遍历后的顺序，存储所有树的结点的引用
        #这时就不会创建任何新的结点（只是创建了个list，引用这些结点而已），而且可以利用这个list调整指向
        l=Solution.get_list(pRootOfTree)
        l_len=len(l)
        #将结点连接起来
        l[0].left=None
        for i in range(l_len-1):
            l[i].right=l[i+1]
            l[i+1].left=l[i]
        l[l_len-1].right=None
        return l[0]

    @staticmethod    
    def get_list(t):
        l=[]
        if t.left is not None: l+=Solution.get_list(t.left)
        l.append(t)#不是把值放进来，是把结点放进来
        if t.right is not None: l+=Solution.get_list(t.right)
        return l