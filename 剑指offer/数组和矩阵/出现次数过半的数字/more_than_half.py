class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        count_each=[0 for x in range(10)]
        n=len(numbers)
        for i in range(n):
            count_each[numbers[i]]+=1
        max_count=max(count_each)
        return count_each.index(max_count) if max_count>n/2 else 0