class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV==None or popV==None:return False#完全不输入肯定算不行
        pop_len=len(popV)#输出序列长度
        push_len=len(pushV)#输入序列长度
        if pop_len is not push_len: return False#长度不同玩个毛
        in_elem=[pushV[0]]#栈
        push_count=1#统计序列中已经入栈了多少个，只加不减
        pop_count=0#统计已经pop了多少个
        for i in range(pop_len):#这个循环是对输出序列的元素一个个判断
            #入栈栈顶元素是否为将要输出元素，以及入栈序列中的元素是否全部入栈了
            while (popV[pop_count] is not in_elem[0]) and (push_count<push_len):
                in_elem.insert(0,pushV[push_count])#入栈
                push_count+=1#入栈元素个数+1
            #全部入栈，且栈顶和即将输出元素不相等，返回false
            if (push_count==push_len) and (in_elem[0] is not popV[pop_count]) :return False
            #基于上面，栈顶和输出序列对比的元素肯定已经相等，可以出栈，pop计数+1
            in_elem.remove(in_elem[0])
            pop_count+=1
        return True