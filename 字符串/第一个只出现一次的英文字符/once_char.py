class Solution:
    def FirstNotRepeatingChar(self, s):
        start_ascii=ord('A')
        alpha_counter=[0 for x in range(ord('z')-ord('A')+1)]
        for i in range(len(s)):
            alpha_counter[ord(s[i])-start_ascii]+=1
        for i in range(len(s)):
            if alpha_counter[ord(s[i])-start_ascii]==1:return i
        return -1