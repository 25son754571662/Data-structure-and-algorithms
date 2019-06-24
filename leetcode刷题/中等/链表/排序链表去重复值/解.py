# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p=head
        if not p:return#没有元素
        if not p.next:return head#只有一个元素
        q=p.next
        #只有两个元素
        if not q.next: return None if q.val==p.val else head
        #有超过两个元素
        #插入头结点，修改p、q指针
        new_head=ListNode('随便写')
        new_head.next=head
        p=new_head
        q=p.next
        r=q.next
        while r and q:
            while r and not q.val==r.val:r,q,p=r.next,q.next,p.next
            while r and q and r.val==q.val:r=r.next
            if q.next:p.next=r
            if p:q=p.next
            if q:r=q.next
        return new_head.next