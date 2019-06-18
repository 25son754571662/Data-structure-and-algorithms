class Solution:
    def FindGreatestSumOfSubArray(self, array):
        max_sum,all_sum,len_arr=array[0],array[0],len(array)
        for i in [x+1 for x in range(len_arr-1)]:
            if array[i]>=0:
                if all_sum<0:all_sum=0
                if all_sum+array[i]>max_sum:max_sum=all_sum+array[i]
            all_sum+=array[i]
        return max(array) if max_sum<0 else max_sum#全负数时还要注意返回最大负数