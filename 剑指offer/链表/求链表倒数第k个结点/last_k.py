class Solution:
    def FindKthToTail(self, head, k):
        p=head
        q=p
        if k==0 or q==None:return None#特殊情况
        for i in range(k-1):#q先跑
            if q.next==None: return None#特殊情况
            q=q.next
        while q.next is not None:#一起跑
            q=q.next
            p=p.next
        return p