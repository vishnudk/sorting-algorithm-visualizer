def maxHeap(l,i):
    if i<len(l):
        v1=v2=-1
        if (i*2)+1<len(l):
            if l[i]<l[(i*2)+1]:
                l[i],l[(i*2)+1]=l[(i*2)+1],l[i]
        if (i*2)+2 < len(l):
            if l[i]<l[(i*2)+2]:
                l[i],l[(i*2)+2]=l[(i*2)+2],l[i]
        maxHeap(l,(i*2)+1)
        maxHeap(l,(i*2)+2)

def function(l):
    sr=[]
    for i in range(len(l)):
        for _ in range(len(l)):
            maxHeap(l,0)
        sr.append(l.pop(0))
    print(sr)
        

if __name__ == "__main__":
    l=[1,2,3,4,5]
    function(l)