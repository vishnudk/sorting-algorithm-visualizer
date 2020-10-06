def merge(l,r):
    # considering that both the array is already sorted 
    arr=[]
    while len(l)>0 and len(r)>0:
        if l[0]>r[0]:
            arr.append(l[0])
            l.pop(0)
        else:
            arr.append(r[0])
            r.pop(0)
    arr.extend(r)
    arr.extend(l)
    return arr

def  mergeSort(arr):
    # print(arr)
    if len(arr)>0:
        if len(arr)==1:
            # print(arr)
            return arr
        else:
            half=int(len(arr)/2)
            l=mergeSort(arr[:half])
            r=mergeSort(arr[half:])
      
            return merge(l,r)
  
def function(l):
    arr = mergeSort(l)
    print(arr)
    



if __name__ == "__main__":
    l=[552, 655, 646, 622, 681, 516, 595, 657, 685, 600, 560, 614, 550, 589]
    # l=[2,2,2,2]
    function(l)
    # print(arr)