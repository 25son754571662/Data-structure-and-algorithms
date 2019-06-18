# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        x1,x2=0 if not l1 else l1.val,0 if not l2 else l2.val
        p1,p2=l1,l2
        while p1.next:
            p1=p1.next
            x1=x1*10+p1.val
        while p2.next:
            p2=p2.next
            x2=x2*10+p2.val
        x=x1+x2
        head=ListNode(x%10)
        x//=10
        while not x==0:
            l=ListNode(x%10)
            l.next=head
            head=l
            x//=10
        return head