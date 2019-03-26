class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        if root==None: return []
        queue=[root]#构建队列，根结点加入队列
        nodes=[]
        while len(queue) is not 0:
            t=queue[0]
            nodes.append(t.val)
            queue.remove(t)
            if t.left is not None: queue.append(t.left)
            if t.right is not None: queue.append(t.right)
        return nodes