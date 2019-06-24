# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        #无奈看了下答案，这么滑稽又巧妙（优秀）的做法真的第一次见，这方法太过分了
        #设置两个指针，一个跑得快，一个跑得慢
        slow_p=fast_p=head
        while fast_p:
            slow_p,fast_p=slow_p.next,fast_p.next
            if not fast_p:return False
            fast_p=fast_p.next
            if slow_p==fast_p:return True
        return False
        