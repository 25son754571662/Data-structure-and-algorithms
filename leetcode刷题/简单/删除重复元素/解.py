# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p=head
        while p:
            q=p.next
            while q and p.val==q.val:q=q.next
            p.next=q
            if p:p=p.next
        return head