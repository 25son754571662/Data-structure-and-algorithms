# array 二维列表
def Find(target, array):
    if array==[] or array==[[]]:return False
    row,col=0,len(array)-1#从右上角开始
    while True:
        #循环执行的条件，但是条件太长所以直接写进这里了
        condition1=(col is not 0) or array[row][col]<target
        condition2=(row is not len(array)-1) or array[row][col]>target
        if not (condition1 and condition2):break
        while array[row][col]>target and col>0:col-=1
        while array[row][col]<target and row<len(array)-1:row+=1
        if array[row][col]==target:return True
    return False

arr=[[1,4,9,13],
     [3,5,11,14],
     [7,9,12,16],
     [9,11,16,20]]
print(Find(12,arr))
print(Find(8,arr))