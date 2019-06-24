# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:return l2
        if not l2:return l1
        #到这步，两个链表都不空
        l=ListNode('head')#创建新的链表(有头结点)
        p1,p2,p=l1,l2,l#指针
        while p1 and p2:#两个指针都还有的时候
            #视情况移动指针
            if p1.val<=p2.val:
                p.next=ListNode(p1.val)
                p1=p1.next
            else: 
                p.next=ListNode(p2.val)
                p2=p2.next
            p=p.next
            if p1: p.next=p1
            if p2: p.next=p2
        return l.next