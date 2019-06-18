class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length=len(rotateArray)
        if length==0 or length==1: return 0 if length==0 else rotateArray[0]
        p=0
        q=length-1
        while True:
            r=int((p+q)/2)
            if rotateArray[r]>rotateArray[p]: p=r
            else: q=r
            if p==q or p==q-1: break
        return min(rotateArray[r],rotateArray[r+1]) if r+1<=length-1 else rotateArray[r]