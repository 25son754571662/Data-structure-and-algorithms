class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        #链表长度3个以内
        if pHead==None or pHead.next==None:return pHead#空表或只有一个
        if pHead.next.next==None:#有两个
            q=pHead.next
            q.next=pHead
            return q
        #链表中元素有三个以上
        p=pHead
        q=p.next
        r=q.next
        while r is not None:
            q.next=p
            if p==pHead: p.next=None
            p=q
            q=r
            r=q.next
        q.next=p
        return q