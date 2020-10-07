# def merge(l,r):
#     # considering that both the array is already sorted 
#     arr=[]
#     while len(l)>0 and len(r)>0:
#         if l[0]>r[0]:
#             arr.append(l[0])
#             l.pop(0)
#         else:
#             arr.append(r[0])
#             r.pop(0)
#     arr.extend(r)
#     arr.extend(l)
#     return arr

# def  mergeSort(arr):
#     # print(arr)
#     if len(arr)>0:
#         if len(arr)==1:
#             # print(arr)
#             return arr
#         else:
#             half=int(len(arr)/2)
#             l=mergeSort(arr[:half])
#             r=mergeSort(arr[half:])
      
#             return merge(l,r)
class meg:
    def __init__(self,arr):
        self.arr=arr
    def merge(self,left,right):
        i=left[1]
        j=right[0]
        for i in range(right[0],right[1]+1):
            while i>left[0]:
                if self.arr[i]>self.arr[i-1]:
                    self.arr[i],self.arr[i-1]=self.arr[i-1],self.arr[i]
                i=i-1
        return list([left[0],right[1]])
    def mergeSOrt(self,start,end):
        if end==start:
            return list([start,end])
        else:
            half=int((start+end)/2)
            left = self.mergeSOrt(start,half)
            right =  self.mergeSOrt(half+1,end)
            return self.merge(left,right)

    
    def function(self):
        arr = self.mergeSOrt(0,len(l)-1)
        print(self.arr)
        



if __name__ == "__main__":
    l=[552, 655, 646, 622, 681, 516, 595, 657, 685, 600, 560, 614, 550, 589]
    # l=[2,2,2,2]
    a=meg(l)
    a.function()
    # print(arr)