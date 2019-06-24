"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:return
        #额外空间法
        l,p,L=[[],[]],head,Node(head.val,None,None)
        q=L
        #1. 生成新的链
        while p:
            l[0].append(p)
            l[1].append(q)
            p=p.next
            if not p:break
            q.next=Node(p.val,None,None)
            q=q.next
        #2. 连接随机指针
        for i in range(len(l[0])):
            p_random=l[0][i].random
            if p_random:#随机指针非空
                idx=l[0].index(p_random)
                l[1][i].random=l[1][idx]
        return L