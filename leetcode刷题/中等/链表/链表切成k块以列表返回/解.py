# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n,p,lst=0,root,[]
        while p:
            n+=1
            p=p.next
        a,b,p=n//k,n%k,root#取整商和余数，后面利用
        for i in range(k):
            lst.append(p)
            n_part=a+(1 if i<b else 0)
            if n_part==0:continue
            for j in range(n_part-1):p=p.next
            q=p.next
            p.next=None
            p=q
        return lst