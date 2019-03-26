class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:return
        #用数组存储整条链，以及整条链的random域的内容
        #下面的三个“l_”开头的变量，都是将对应引用存储为数组
        l_link,l_random,p,=[],[],pHead
        l_new_link=[RandomListNode(p.label)]
        new_link=l_new_link[0]
        q=new_link
        while p:#一边读入，一边重建链
            #读入
            l_link.append(p)
            l_random.append(p.random)
            #重建链
            q.next=RandomListNode(p.next.label)if p.next else None
            l_new_link.append(q.next)
            #移动指针
            q,p=q.next,p.next
        #连接random域
        for count in range(len(l_link)-1):
            if l_random[count]:
                index=l_link.index(l_random[count])
                l_new_link[count].random=l_new_link[index]
        return new_link