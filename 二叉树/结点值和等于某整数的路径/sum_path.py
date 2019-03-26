class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        paths=[[x.val for x in node] for node in self.GetAllPath(root)]
        is_legal=[sum(path)==expectNumber for path in paths]
        legal_paths=[]
        for i in range(len(is_legal)):
            if is_legal[i]:legal_paths.append(paths[i])        
        return legal_paths
    def GetAllPath(self,root):
        if not root:return []
        a=[root]
        b=self.GetAllPath(root.left)
        c=self.GetAllPath(root.right)
        if b==[] and c==[]:return [a]
        return [a+x for x in b]+[a+x for x in c]