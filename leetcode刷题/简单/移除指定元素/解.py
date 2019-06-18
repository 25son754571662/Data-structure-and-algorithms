# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:return
        p=head
        while p:
            if p.val==val:p=p.next
            else:break
        q=p
        while q:
            if q.next and q.next.val==val:q.next=q.next.next
            else:q=q.next
        return p