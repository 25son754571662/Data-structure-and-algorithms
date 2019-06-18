# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        
        if not head:return
        
        n,p=0,head
        
        #先计算链表长度
        while p:
            n+=1
            p=p.next
            
        #得到不超过n的新k
        new_k=k%n
        if new_k==0:return head
        
        #通过指针来改变链接
        p=q=head
        for i in range(new_k):q=q.next#指针q先走new_k步
        while q.next:p,q=p.next,q.next#两个指针一起走到底
        new_head,q.next,p.next=p.next,head,None
        
        return new_head
        
            