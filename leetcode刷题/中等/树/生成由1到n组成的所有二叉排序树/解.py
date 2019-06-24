# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return [] if n==0 else self.generateTree([x+1 for x in range(n)])
        
    def generateTree(self,l_num):
        n,l_tree=len(l_num),[]
        if n==0:return [None]
        if n==1:return [TreeNode(l_num[0])]
        for i in range(n):
            left_part,right_part=self.generateTree(l_num[:i]),self.generateTree(l_num[i+1:])
            n_left,n_right=len(left_part),len(right_part)
            for j in range(n_left):
                for k in range(n_right):
                    temp=TreeNode(l_num[i])
                    temp.left,temp.right=left_part[j],right_part[k]
                    l_tree.append(temp)
        return l_tree