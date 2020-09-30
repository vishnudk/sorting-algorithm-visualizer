def function(arr,i,j):
    pivot=i
    end=j
    while j>=i and j>pivot and i<end:
        if arr[i]>=arr[pivot]:
            i=i+1
        if arr[j]<=arr[pivot]:
            j=j-1
        if j>i and arr[i]<arr[pivot] and arr[j]>arr[pivot]:
            arr[i],arr[j]=arr[j],arr[i]
        # print(arr)
    arr[j],arr[pivot]=arr[pivot],arr[j]
    if j-1>pivot:
        function(arr,pivot,j-1)
    if j+1<end:
        function(arr,j+1,end)




if __name__ == "__main__":
    # arr=[1,4,2,6,10,7]
    arr=[520, 601, 679, 540, 574, 634, 671, 575, 643, 538, 515, 584, 678, 524, 515, 575, 542, 639, 507, 663, 545, 641, 654, 617, 605, 697, 666, 507, 655]
    arr.append(float('-inf'))
    function(arr,0,len(arr)-1)
    arr.pop()
    print(arr)




    #=======================================================================================






    
        self.pivot=self.prvI=arg[0]
        self.end=self.prvJ=arg[1]
        self.count=1
  
        while self.prvJ>=self.prvI and self.prvJ>self.pivot and self.prvI<self.end:
            if self.array[self.prvI]>=self.array[self.pivot]:
                self.prvI=self.prvI+1   
            if self.array[self.prvJ]<=self.array[self.pivot]: 
                self.prvJ=self.prvJ-1 
            if self.prvJ>self.prvI and self.array[self.prvI]<self.array[self.pivot] and self.array[self.prvJ]>self.array[self.pivot]:
                self.array[self.prvI],self.array[self.prvJ]=self.array[self.prvJ],self.array[self.prvI]
                self.line[self.prvI],self.line[self.prvJ]=self.line[self.prvJ],self.line[self.prvI]  
        self.array[self.prvJ],self.array[self.pivot]=self.array[self.pivot],self.array[self.prvJ]
        tmpI=self.prvI
        tmpJ=self.prvJ
        tmpPivot=self.pivot
        tmpEnd=self.end
        if tmpJ-1>tmpPivot:
            self.count=0
            self.QickSort(tmpPivot,tmpJ-1)
        if tmpJ+1<tmpEnd:
            self.count=0
            self.QickSort(tmpJ+1,tmpEnd) 



#===============================v2=================





if self.count==0:
            self.pivot=self.prvI=arg[0]
            self.end=self.prvJ=arg[1]
            self.count=1
            self.CheckLine1=self.canvas.create_line(self.canvas.coords(self.line[self.pivot])[0],max(self.array),self.canvas.coords(self.line[self.pivot])[2],self.canvas.coords(self.line[self.pivot])[3],width=10,fill='green')
            self.CheckLine2=self.canvas.create_line(self.canvas.coords(self.line[self.end])[0],max(self.array),self.canvas.coords(self.line[self.end])[2],self.canvas.coords(self.line[self.end])[3],width=10,fill='green')
            self.canvas.after(20,self.QickSort)
  
        while self.prvJ>=self.prvI and self.prvJ>self.pivot and self.prvI<self.end:
            self.canvas.move(self.CheckLine1,10,0)
            self.canvas.move(self.CheckLine1,-10,0)
            if self.array[self.prvI]>=self.array[self.pivot]:
                self.prvI=self.prvI+1   
                self.canvas.move(self.CheckLine1,10,0)
                # self.canvas.after(100,self.QickSort)
            if self.array[self.prvJ]<=self.array[self.pivot]: 
                self.prvJ=self.prvJ-1 
                self.canvas.move(self.CheckLine1,-10,0)
                # self.canvas.after(100,self.QickSort)
            if self.prvJ>self.prvI and self.array[self.prvI]<self.array[self.pivot] and self.array[self.prvJ]>self.array[self.pivot]:
                self.array[self.prvI],self.array[self.prvJ]=self.array[self.prvJ],self.array[self.prvI]
                self.line[self.prvI],self.line[self.prvJ]=self.line[self.prvJ],self.line[self.prvI]  
                # self.canvas.after(20,self.QickSort)
            self.canvas.after(20,self.QickSort)
        self.array[self.prvJ],self.array[self.pivot]=self.array[self.pivot],self.array[self.prvJ]
        tmpI=self.prvI
        tmpJ=self.prvJ
        tmpPivot=self.pivot
        tmpEnd=self.end
        if tmpJ-1>tmpPivot:
            # time.sleep(1)
            try:
                self.canvas.delete(self.CheckLine1)
                self.canvas.delete(self.CheckLine2)
            except:
                pass
            self.count=0
            self.QickSort(tmpPivot,tmpJ-1)
        if tmpJ+1<tmpEnd:
            # time.sleep(1)
            try:
                self.canvas.delete(self.CheckLine1)
                self.canvas.delete(self.CheckLine2)
            except:
                pass
            self.count=0
            self.QickSort(tmpJ+1,tmpEnd)




#============================================================================            