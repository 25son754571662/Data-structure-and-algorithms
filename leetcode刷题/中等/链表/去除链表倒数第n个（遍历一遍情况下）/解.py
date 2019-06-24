# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p=q=head#两个指针一起走，简单
        for i in range(n):q=q.next#q先走
        if not q:return head.next#特例，n刚好等于总个数
        while q.next:p,q=p.next,q.next#一起走
        p.next=p.next.next
        return head