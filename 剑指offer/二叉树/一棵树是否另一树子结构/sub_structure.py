class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        if pRoot2==None: return False#空树不是任意一个树的子结构
        if pRoot1==None: return False#空树不可能成为任意一棵树的结构
        #根结点是否满足，满足的话直接返回True
        condition1=pRoot1.val==pRoot2.val
        condition2=True if not pRoot2.left else self.HasSubtree(pRoot1.left,pRoot2.left)
        condition3=True if not pRoot2.right else self.HasSubtree(pRoot1.right,pRoot2.right)
        if condition1 and condition2 and condition3:return True
        #判断B是不是A左子树的子结构，如果是，返回True
        if self.HasSubtree(pRoot1.left,pRoot2):return True
        #判断B是不是A右子树的子结构，如果是，返回True
        if self.HasSubtree(pRoot1.right,pRoot2):return True
        #所有情况都不满足，返回False
        return False