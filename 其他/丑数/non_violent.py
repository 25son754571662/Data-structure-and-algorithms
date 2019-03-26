class Solution:
    def GetUglyNumber_Solution(self, index):
        if index==1:return 1
        if index<=0:return 0
        #那个用三个队列的方法实在太牛逼了
        #这都能想出来，这玩意我想了一下午，还弄了个树出来了都做不出
        u_numbers,queue_2,queue_3,queue_5=[1],[2],[3],[5]
        for i in range(index-1):
            top_elems=[queue_2[0],queue_3[0],queue_5[0]]
            min_num=min(top_elems)
            if queue_2[0]==min_num:queue_2.pop(0)
            if queue_3[0]==min_num:queue_3.pop(0)
            if queue_5[0]==min_num:queue_5.pop(0)
            u_numbers.append(min_num)
            queue_2.append(2*min_num)
            queue_3.append(3*min_num)
            queue_5.append(5*min_num)
        return u_numbers[index-1]