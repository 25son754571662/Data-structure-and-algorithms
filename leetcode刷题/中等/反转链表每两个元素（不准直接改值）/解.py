# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:return head
        #反转前两个
        p=head.next
        head.next=head.next.next
        p.next=head
        #递归反转后面的结点
        head.next=self.swapPairs(head.next)
        return p