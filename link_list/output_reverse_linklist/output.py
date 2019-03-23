def printListFromTailToHead(listNode):
    p=listNode
    arr_list=[]
    while p is not None:
        arr_list.insert(0,p.val)
        p=p.next
    return arr_list