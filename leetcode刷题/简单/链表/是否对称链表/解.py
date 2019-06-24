# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l,lr,p=[],[],head
        while p:
            l.append(p.val)
            lr.append(p.val)
            p=p.next
        lr.reverse()
        return l==lr