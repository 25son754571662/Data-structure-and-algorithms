class InversePair:
    @staticmethod
    def InversePairs(data):
        _, s = InversePair.MergeSort(data)
        return s
    @staticmethod
    def MergeSort(data):
        n = len(data)
        # 递归基
        if n == 1: return data, 0
        # 分两半来排序
        part1, part2 = data[:n // 2], data[n // 2:]
        sorted_part1, s1 = InversePair.MergeSort(part1)
        sorted_part2, s2 = InversePair.MergeSort(part2)
        # 排序后拼接，拼接后先计数，然后将两个有序序列排序
        s, sorted_temp = 0, sorted_part1 + sorted_part2
        # 用p、q两个指针指向两段，计算q中每个元素离插入点的index差
        p, q, len1, len_all = 0, sorted_temp.index(sorted_part2[0]), len(sorted_part1), len(sorted_temp)
        while p < len1 and q < len_all:
            # 移动p使p成为插入排序的插入点
            while p < len1:
                if sorted_temp[q] < sorted_temp[p]:
                    s += len1 - p
                    break
                p += 1
            q += 1
        # 完成排序，并把排序后的内容回溯给上一级做准备
        l = []
        p, q = 0, sorted_temp.index(sorted_part2[0])
        while p < len1 and q < len_all:
            if sorted_temp[p] < sorted_temp[q]:
                l.append(sorted_temp[p])
                p += 1
            else:
                l.append(sorted_temp[q])
                q += 1
        if p == len1: l += sorted_temp[q:]
        if q == len_all: l += sorted_part1[p:]
        return l, s + s1 + s2

print(InversePair.InversePairs([7,3,2,9,1,6,4,5,8]))