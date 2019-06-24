# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        n,p=0,head
        while p:
            n+=1
            p=p.next
        p=head
        for i in range(n//2):p=p.next
        return p