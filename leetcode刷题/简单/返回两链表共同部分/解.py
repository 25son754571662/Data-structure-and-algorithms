# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:return None
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        count1,count2,p1,p2=0,0,headA,headB
        #遍历一遍，看链有多长
        while p1:
            count1+=1
            p1=p1.next
        while p2:
            count2+=1
            p2=p2.next
        delta=count1-count2
        #错开距离一起走
        p1,p2=headA,headB
        if delta>0:
            for i in range(delta):p1=p1.next
        if delta<0:
            for i in range(-delta):p2=p2.next
        while p1:
            if p1==p2:return p1
            p1,p2=p1.next,p2.next
        return None
                