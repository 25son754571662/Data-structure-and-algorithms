# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p,q=l1,l2
        head=ListNode((p.val+q.val)%10)
        temp=ListNode(0)
        last=(p.val+q.val)//10
        r=head
        while p.next or q.next:
            p,q=p.next if p.next else temp,q.next if q.next else temp
            p_new=ListNode((last+p.val+q.val)%10)
            last=(last+p.val+q.val)//10
            r.next=p_new
            r=r.next
        if last>0:r.next=ListNode(last)
        return head