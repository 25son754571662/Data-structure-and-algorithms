class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        if root==None:return None#根结点为空
        #根结点不空，就有左右指针，交换根结点左右指针
        t=root.left
        root.left=root.right
        root.right=t
        #对左子树实行镜像
        Solution.Mirror(self,root.left)
        #对右子树实行镜像
        Solution.Mirror(self,root.right)
        return root