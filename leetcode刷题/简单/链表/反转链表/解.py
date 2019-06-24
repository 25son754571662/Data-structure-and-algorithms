# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        p=head
        if not p:return None#没有元素返回空
        if not p.next:return head#只有一个元素，反转都一样
        q=p.next#不止一个元素，可以有next
        if not q.next:#只有两个元素
            p=head.next
            head.next.next=head
            head.next=None
            return p
        #有三个元素以上，可以再有next
        r=q.next
        p.next=None#头结点改为空指针
        while r:#最后一个指针不为空
            q.next=p
            p=q
            q=r
            r=r.next
        q.next=p
        return q