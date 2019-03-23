class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1==None: return pHead2
        if pHead2==None: return pHead1
        #此时，两条链链头都有元素
        p1,p2=pHead1,pHead2
        #创建一条新链
        pHead,is_equal=ListNode(min(p1.val,p2.val)),p1.val==p2.val
        if is_equal:pHead.next=ListNode(p1.val)
        p=pHead.next if is_equal else pHead
        while p1 and p2:
            #不同情况指针的移动
            if p1.val<p2.val:p1=p1.next
            elif p2.val<p1.val:p2=p2.next
            else:p1,p2=p1.next,p2.next
            #p1或p2到结尾了
            if not p1:
                p.next=p2
                break
            if not p2:
                p.next=p1
                break
            #不等和相等两种情况，插入也有不同
            if not p1.val==p2.val:
                p.next=ListNode(min(p1.val,p2.val))
                p=p.next
            else:
                p.next=ListNode(p1.val)
                p.next.next=ListNode(p1.val)
                p=p.next.next
        return pHead