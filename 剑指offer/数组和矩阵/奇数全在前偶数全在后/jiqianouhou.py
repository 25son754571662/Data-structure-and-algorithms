class Solution:
    def reOrderArray(self, array):
        # write code here
        #我看看尽量写个空间复杂度低的，不过算了，还是老老实实弄两个存储单元
        arr_single=[]
        arr_oval=[]
        for i in range(len(array)):
            if array[i]%2==0:arr_oval.append(array[i])
            else: arr_single.append(array[i])
        return arr_single+arr_oval