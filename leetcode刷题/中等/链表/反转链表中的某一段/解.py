# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m==n:return head
        part_head=mid_tail=head#前部分的尾指针、后部分的头指针和中间部分的尾指针
        for i in range(m-2):part_head=part_head.next
        for i in range(n-1):mid_tail=mid_tail.next
        mid_head=part_head.next if m>=2 else head
        part_tail=mid_tail.next
        ending=part_tail
        while ending and ending.next:ending=ending.next
        #对中间部分逆序
        p=mid_head
        if m-n==1:#两个元素，直接逆吧
            q=p.next
            q.next=p
            p.next=None
            mid_head,mid_tail=q,p
        else:
            q=p.next
            r=q.next
            p.next=None
            mid_tail=p
            while not r==part_tail:
                q.next=p
                p=q
                q=r
                r=r.next
            q.next=p
            mid_head=q
        #最后的连接
        if m>=2:#普通情况
            part_head.next=mid_head
        else:
            head=mid_head
        mid_tail.next=part_tail
                
        return head
            
            
        