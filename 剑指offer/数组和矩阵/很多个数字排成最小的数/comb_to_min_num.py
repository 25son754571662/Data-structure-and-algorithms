class Solution:
    def PrintMinNumber(self, numbers):
        if numbers==[]:return ""
        # 转成list形式
        l = [[x // pow(10, len(str(x)) - bit - 1) % 10 for bit in range(len(str(x)))] for x in numbers]
        get_l = self.GetMinSerial(l)
        n = len(get_l)
        return sum([10 ** i * get_l[n - i - 1] for i in range(n)])
    
    def GetMinSerial(self, l):
        if l == []: return
        n = len(l)
        if n == 1: return l[0]
        # 思路：找到应该放到开头的数字，然后递归后面的
        p_l = [0 for x in range(n)]
        max_p_l = [len(l[x]) - 1 for x in range(n)]
        # 移动指针，直到有唯一可以放开头的，或者直到指针已经都移到尽头
        while True:
            p_values = [l[i][p_l[i]] for i in range(n)]
            min_p_value = min(p_values)
            is_min = [x == min_p_value for x in p_values]
            if sum(is_min) == 1: break  # 找到唯一可以放开头的，跳出循环
            if p_l == max_p_l: break#指针全到尽头，不再移动指针
            for i in range(n):
                if is_min[i] and p_l[i]<max_p_l[i]: p_l[i] += 1  # 继续移动指针
        #指针移动到合适的位置后
        if sum(is_min) == 1:  # 找到唯一可以放开头的
            index = p_values.index(min_p_value)
            return l.pop(index) + self.GetMinSerial(l)
        else:  # 全程没有唯一可以放开头的，直接全部拼接起来就好了
            temp = l[0]
            for i in range(n - 1):
                temp += l[i + 1]
            return temp