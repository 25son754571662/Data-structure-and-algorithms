# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        #搞了半天原来是删除当前结点的值
        p=node
        if not p.next:p=None
        p.val=p.next.val
        p.next=p.next.next