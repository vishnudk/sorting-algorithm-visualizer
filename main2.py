import multiprocessing as mp
# import numpy
import mergeSort as ms
from tkinter import *
from speech_virus import voice
import random
import time
import os
# from ttkthemes import themed_tk as tk
# # from ttkthemes import themed_tk
# from ttkthemes import ThemedTk
import signal
from tkinter import ttk

# class for node of tree
class node:
    def __init__(self,data):
        self.data=data
        self.leftNode=None
        self.rightNode=None
        
class App:
    def __init__(self,canvas,app):
        self.canvas=canvas
        self.app=app
        self.array=[]
        self.arrayLength=0
        self.arraySize=0
        self.line=[]
        self.CheckLine=-1
        self.coords=[]
        self.index=1
        self.max=-1
        self.pos = 0
        self.prvI=-1
        self.prvJ=0
        self.count=0
        self.maxPos=0
        self.prvArraySize=0
        self.activate=0
        self.searchSpeed=2
        self.flag=0
        self.pivot=0
        self.end=0
        self.CheckLine1=-1
        self.CheckLine2=-1
    def reInit(self):
        # self.canvas=canvas
        # self.app=app
        # self.array=[]
        # self.arrayLength=0
        # self.arraySize=0
        self.line=[]
        self.CheckLine=-1
        # self.coords=[]
        self.index=1
        self.max=-1
        self.pos = 0
        self.prvI=-1
        self.prvJ=0
        self.count=0
        self.maxPos=0
        self.prvArraySize=0
        self.activate=0
        # self.searchSpeed=2
        self.flag=0
        self.pivot=0
        self.end=0
        self.CheckLine1=-1
        self.CheckLine2=-1
    def merge(self,l,r,line,line1):
    # considering that both the array is already sorted 
        arr=[]
        # while len(l)>0 and len(r)>0:
        #     if l[0]>r[0]:
        #         arr.append(l[0])
        #         l.pop(0)
        #     else:
        #         arr.append(r[0])
        #         r.pop(0)
        # arr.extend(r)
        # arr.extend(l)
        j=0
        i=len(l)-1
        while i>=0 and j<len(r):
            if l[i]>r[j]:
                j=j+1
            

        return arr

    def  mergeSort(self,arr,start,end):
        # print(arr)
        if len(arr)>0:
            if len(arr)==1:
                # print(arr)
                return arr
            else:
                half=int((start+end)/2)
                l=self.mergeSort(arr[:half],start,half-1)
                lp=list([start,half-1])
                r=self.mergeSort(arr[half:],half,end)
                rp=list([half,end])

                return self.merge(l,r,self.line[start:half],self.line[half:end],lp,rp)
    def callMergeSort(self):
        print(self.array)
        self.array=self.mergeSort(self.array,0,len(self.array)-1)
        self.printArray()
    def maxHeap(self,i):
        if i>0:
            try:
                self.canvas.delete(self.CheckLine)
            except:
                pass
            try:
                self.canvas.delete(self.CheckLine1)
            except:
                pass
            if i%2==0:
                childLinePos=self.canvas.coords(self.line[i])
                childLinePos[1]=max(self.array)
                self.CheckLine=self.canvas.create_line(childLinePos)
                root=int((i-2)/2)
                rootLinePos=self.canvas.coords(self.line[root])
                rootLinePos[1]=max(self.array)
                self.CheckLine1=self.canvas.create_line(rootLinePos)
                self.canvas.after(20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
                if self.array[root]>self.array[i]:
                    self.array[root],self.array[i]=self.array[i],self.array[root]
                    self.canvas.move(self.line[i],(root-i)*10,0)
                    self.canvas.move(self.line[root],(i-root)*10,0)
                    self.canvas.after(20-int(self.searchSpeed))
                    self.canvas.update_idletasks()
                    self.canvas.update()
                    self.line[root],self.line[i]=self.line[i],self.line[root]


                    
                self.maxHeap(i-1)
            else:
                childLinePos=self.canvas.coords(self.line[i])
                childLinePos[1]=max(self.array)
                self.CheckLine=self.canvas.create_line(childLinePos,width=10,fill='green')
                root=int((i-1)/2)
                rootLinePos=self.canvas.coords(self.line[root])
                rootLinePos[1]=max(self.array)
                self.CheckLine1= self.canvas.create_line(rootLinePos,width=10,fill='green')
                self.canvas.after(20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
                if self.array[root]>self.array[i]:
                    self.array[root],self.array[i]=self.array[i],self.array[root]
                    self.canvas.move(self.line[i],(root-i)*10,0)
                    self.canvas.move(self.line[root],(i-root)*10,0)
                    self.canvas.after(20-int(self.searchSpeed))
                    self.canvas.update_idletasks()
                    self.canvas.update()
                    self.line[root],self.line[i]=self.line[i],self.line[root]
                self.maxHeap(i-1)
        
    def heapSort(self):
        sr=[]
        lines=[]
        for i in range(len(self.array)):
            # for _ in range(len(self.array)):
            self.maxHeap(len(self.array)-1)
            try:
                self.canvas.delete(self.CheckLine)
            except:
                pass
            try:
                self.canvas.delete(self.CheckLine1)
            except:
                pass
            sr.append(self.array.pop(0))  
            self.canvas.move(self.line[0],10*(len(self.array)),0)
            self.canvas.itemconfig(self.line[0],fill='blue')
            lines.append(self.line.pop(0))
            for i in range(len(self.line)):
                self.canvas.move(self.line[i],-10,0)
            # self.line[0],self.line[len(self.array)]=self.line[len(self.array)],self.line[0]
            self.canvas.after(20-int(self.searchSpeed))
            self.canvas.update_idletasks()
            self.canvas.update()
        self.array=sr[:]
        for i in lines:

            self.canvas.itemconfig(i,fill='red')
        # print(self.array)
    def callHeapSort(self):
        l2=Label(self.app, text = "Heap Sort") 
        l2.place(x=600,y=10)
        self.heapSort()
        # self.printArray()
    def QickSort(self,*arg):
        if self.count==0:
           
            self.pivot=self.prvI=arg[0]
            self.end=self.prvJ=arg[1]
            self.count=1
            self.CheckLine1=self.canvas.create_line(self.canvas.coords(self.line[self.pivot])[0],max(self.array),self.canvas.coords(self.line[self.pivot])[2],self.canvas.coords(self.line[self.pivot])[3],width=10,fill='green')
            self.CheckLine2=self.canvas.create_line(self.canvas.coords(self.line[self.end])[0],max(self.array),self.canvas.coords(self.line[self.end])[2],self.canvas.coords(self.line[self.end])[3],width=10,fill='green')
           
  
        while self.prvJ>=self.prvI and self.prvJ>self.pivot and self.prvI<self.end:
  
            if self.array[self.prvI]>=self.array[self.pivot] :
                self.prvI=self.prvI+1   
                self.flag=1
                self.canvas.move(self.CheckLine1,10,0)
                self.canvas.after(20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
            if self.prvJ>self.prvI and self.array[self.prvI]<self.array[self.pivot] and self.array[self.prvJ]>self.array[self.pivot]:
                self.array[self.prvI],self.array[self.prvJ]=self.array[self.prvJ],self.array[self.prvI]
                self.canvas.move(self.line[self.prvI],(self.prvJ-self.prvI)*10,0)
                self.canvas.move(self.line[self.prvJ],(self.prvI-self.prvJ)*10,0)
                self.line[self.prvI],self.line[self.prvJ]=self.line[self.prvJ],self.line[self.prvI]  
                self.canvas.after(20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
                
                   
            if   self.array[self.prvJ]<=self.array[self.pivot] : 
                self.prvJ=self.prvJ-1 
                self.canvas.move(self.CheckLine2,-10,0)
                self.flag=2
                self.canvas.after( 20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
              
            
               
           
       
        self.array[self.prvJ],self.array[self.pivot]=self.array[self.pivot],self.array[self.prvJ]
       
        # if arg[1]-arg[0]<=2:
        #     for pos in range(arg[0],arg[1]+1):
        #         self.canvas.itemconfig(self.line[pos],fill='blue')
        # else:
        self.canvas.itemconfig(self.line[self.pivot],fill='blue')
        self.canvas.move(self.line[self.pivot],(self.prvJ-self.pivot)*10,0)
        self.canvas.move(self.line[self.prvJ],(self.pivot-self.prvJ)*10,0)
        
        self.line[self.prvJ],self.line[self.pivot]=self.line[self.pivot],self.line[self.prvJ]
        tmpI=self.prvI
        tmpJ=self.prvJ
        tmpPivot=self.pivot
        tmpEnd=self.end
        if tmpJ-1>tmpPivot:
            try:
                self.canvas.delete(self.CheckLine1)
            except:
                pass
            try:
                self.canvas.delete(self.CheckLine2)
            except:
                pass
            self.flag=0
            self.count=0
            # newpid = os.fork()
            # p1 = mp.Process(target= self.QickSort(tmpPivot,tmpJ-1))
            self.QickSort(tmpPivot,tmpJ-1)
            
            # os.kill(newpid, signal.SIGKILL)
            for pos in range(tmpPivot,tmpJ-1):
                self.canvas.itemconfig(self.line[pos],fill='blue')
        if tmpJ+1<tmpEnd:
            try:
                self.canvas.delete(self.CheckLine1)
            except:
                pass
            try:
                self.canvas.delete(self.CheckLine2)
            except:
                pass
            self.flag=0
            self.count=0
            # newpid = os.fork()
            # p2 = mp.Process(target= self.QickSort(tmpJ+1,tmpEnd) )
            self.QickSort(tmpJ+1,tmpEnd)
            # os.kill(newpid, signal.SIGKILL)
            for pos in range(tmpJ+1,tmpEnd+1):
                self.canvas.itemconfig(self.line[pos],fill='blue')
        # try:self.canvas.itemconfig(self.
        #     p1.start()
        # except:
        #     pass
        # try:
        #     p2.start()
        # except:
        #     pass
        # try:
        #     p1.join()
        # except:
        #     pass

    def CallQuicksort(self):
        l2=Label(self.app, text = "Quick Sort") 
        l2.place(x=600,y=10)
       
        self.QickSort(0,self.arrayLength-1)
        try:
            self.canvas.delete(self.CheckLine1)
           
        except:
            pass
        try:
           
            self.canvas.delete(self.CheckLine2)
        except:
            pass
        
        for i in range(len(self.line)):
            self.canvas.itemconfig(self.line[i],fill='red')
            
      
        
        self.reInit()
    def bubbleSort(self):
        if self.count==0:
            try:
                self.canvas.delete(self.CheckLine)
            except:
                pass
            self.count=1
            self.prvI=self.prvI+1
            self.CheckLine = self.canvas.create_line(self.canvas.coords(self.line[0])[0],max(self.array),self.canvas.coords(self.line[0])[2],self.canvas.coords(self.line[0])[3],width=10,fill='green')
        while self.prvI<self.arrayLength:
            while self.prvJ<self.arrayLength-1-self.prvI:
              
                if self.flag==0:
                    self.canvas.move(self.CheckLine,10,0)
                    self.flag=1
                    self.canvas.after(20-int(self.searchSpeed))
                    self.canvas.update_idletasks()
                    self.canvas.update()
                if self.flag==1:
                    self.canvas.move(self.CheckLine,-10,0)
                    self.flag=2
                    self.canvas.after(20-int(self.searchSpeed))
                    self.canvas.update_idletasks()
                    self.canvas.update()
                self.flag=0
                self.canvas.move(self.CheckLine,10,0)
                if self.array[self.prvJ]<self.array[self.prvJ+1]:
                    self.array[self.prvJ],self.array[self.prvJ+1]=self.array[self.prvJ+1],self.array[self.prvJ]
                    self.canvas.move(self.line[self.prvJ],10,0)
                    self.canvas.move(self.line[self.prvJ+1],-10,0)
                    self.line[self.prvJ],self.line[self.prvJ+1]=self.line[self.prvJ+1],self.line[self.prvJ]
                self.prvJ=self.prvJ+1
                self.canvas.after(20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
            if self.prvJ>=self.arrayLength-1-self.prvI:
                self.canvas.delete(self.CheckLine)
                self.CheckLine = self.canvas.create_line(self.canvas.coords(self.line[0])[0],max(self.array),self.canvas.coords(self.line[0])[2],self.canvas.coords(self.line[0])[3],width=10,fill='green')
                self.canvas.itemconfig(self.line[self.arrayLength-1-self.prvI],fill='blue')
                self.prvI=self.prvI+1
                self.prvJ=0
                self.canvas.after(20-int(self.searchSpeed))
                self.canvas.update_idletasks()
                self.canvas.update()
            
    
        self.canvas.itemconfig(self.line[0],fill='blue')
        self.canvas.delete(self.CheckLine)
        self.prvJ=self.prvI=0
        for i in range(len(self.line)):
            self.canvas.itemconfig(self.line[i],fill='red')
        self.reInit()
       
    def callBubbleSort(self):
        l2=Label(self.app, text = "Bubble Sort") 
        l2.place(x=600,y=10)
        self.bubbleSort()
        
        
       
    def selectionSort(self):
        l2=Label(self.app, text = "Selection Sort") 
        l2.place(x=600,y=10)
        while self.prvI<self.arrayLength-1:
            if self.prvJ>=self.arrayLength or self.count==0:
                try :
                    self.canvas.delete(self.CheckLine)
                except:
                    pass
                self.CheckLine = self.canvas.create_line(self.canvas.coords(self.line[self.prvI+1])[0],max(self.array),self.canvas.coords(self.line[self.prvI+1])[2],self.canvas.coords(self.line[self.prvI+1])[3],width=10,fill='green')
                # print(self.coords[self.prvI+1])
                
                # self.CheckLine = self.canvas.create_line(self.coords[self.prvI+1],fill='green')
                self.count=1
                self.prvI=self.prvI+1
                self.prvJ=self.prvI+1
                self.max = self.array[self.prvI]
                self.pos=self.prvI
            while self.prvJ<self.arrayLength:
                self.canvas.move(self.CheckLine,10,0)
                if self.max<self.array[self.prvJ]:
                    self.pos=self.prvJ
                    self.max=self.array[self.prvJ]
                self.prvJ=self.prvJ+1
                break
            if self.prvJ>=self.arrayLength:
                self.array[self.prvI],self.array[self.pos]=self.array[self.pos],self.array[self.prvI]
                self.canvas.move(self.line[self.prvI],(self.pos-self.prvI)*10,0)
                self.canvas.move(self.line[self.pos],(self.prvI-self.pos)*10,0)
                # self.coords[self.prvI],self.coords[self.pos]=self.coords[self.pos],self.coords[self.prvI]
                self.coords[self.prvI][0],self.coords[self.pos][0]=self.coords[self.pos][0],self.coords[self.prvI][0]
                self.coords[self.prvI][2],self.coords[self.pos][2]=self.coords[self.pos][2],self.coords[self.prvI][2]
                self.line[self.prvI],self.line[self.pos]=self.line[self.pos],self.line[self.prvI]
                self.canvas.itemconfig(self.line[self.prvI],fill='blue')
                
            break


        if self.prvI<self.arrayLength-1:
            self.canvas.after(21-int(self.searchSpeed),self.selectionSort)
        else:
            self.canvas.delete(self.CheckLine)
            # print (self.array)
            for i in range(len(self.line)):
                self.canvas.itemconfig(self.line[i],fill='red')
            self.reInit()
     
      
    def checkArraySize(self,size):
        if size != self.prvArraySize:
            self.prvArraySize=size
            self.createRandomArray()  

    def printArray(self):
        self.canvas.delete("all")
        x=(int(self.canvas.winfo_screenmmwidth()/2)-((self.arrayLength/2)*10))+550
        for i in range(self.arrayLength):
            self.line.append(self.canvas.create_line(x+(i*10),self.array[i], x+(i*10), 100,width=9))
            self.coords.append([x+(i*10),self.array[i], x+(i*10), 100])
    def createRandomArray(self):
        self.index=1
        self.max=-1
        self.pos = 0
        self.prvI=-1
        self.prvJ=1
        self.count=0
        self.maxPos=0
        self.array=[]
        self.arrayLength=0
        self.line=[]
        self.coords=[]
        self.index=1
        self.prv = -1
        self.count=0
        self.activate=0
        self.canvas.delete("all")
        self.array=[]
        self.line=[]
        self.arrayLength=self.arraySize.get()
        for i in range(self.arrayLength):
            self.array.append(random.randint(500,700))
        
        x=(int(self.canvas.winfo_screenmmwidth()/2)-((self.arrayLength/2)*10))+550

        for i in range(self.arrayLength):
            self.line.append(self.canvas.create_line(x+(i*10),self.array[i], x+(i*10), 100,width=9))
            self.coords.append([x+(i*10),self.array[i], x+(i*10), 100])
        tmpList=[]
        tmpList2=[]
        for i in self.coords:
            tmpList.append(i)
        for i in self.line:
            tmpList2.append(self.canvas.coords(i))
        # if tmpList==tmpList2:
            # print("True")
    def changeSpeed(self,newSpeed):
        self.searchSpeed=newSpeed  
    def mainFunction(self):
        # array selection region
        l=Label(self.app, text = "Array Size") 
        l.place(x=0,y=10)
        self.arraySize = Scale(self.app, from_=0, to=140, orient=HORIZONTAL, command=self.checkArraySize)
        self.arraySize.place(x=80,y=0) 
        button = Button(self.app, text='create', width=10, command=self.createRandomArray)
        button.place(x=200,y=10)
        l2=Label(self.app, text = "Searching Speed") 
        l2.place(x=300,y=10)
        searchSpeedScale = Scale(self.app, from_=0, to=20, orient=HORIZONTAL, command=self.changeSpeed)
        searchSpeedScale.place(x=400,y=0)
       
       
        #menu
        menu = Menu(self.app) 
        self.app.config(menu=menu) 
        filemenu = Menu(menu) 
        menu.add_cascade(label='File', menu=filemenu) 
        filemenu.add_command(label='New') 
        filemenu.add_command(label='Open...') 
        # filemenu.add_separator() 
        filemenu.add_command(label='Exit', command=self.app.quit) 
        helpmenu = Menu(menu) 
        menu.add_cascade(label='Help', menu=helpmenu) 
        helpmenu.add_command(label='About') 
        algoritmMenu=Menu(menu)
        menu.add_cascade(label='Algorithms',menu=algoritmMenu)
        algoritmMenu.add_command(label='Buble sort',command=self.callBubbleSort)
        algoritmMenu.add_command(label='Quick sort',command=self.CallQuicksort)
        algoritmMenu.add_command(label='Selection sort',command=self.selectionSort)
        algoritmMenu.add_command(label='Merge sort',command=self.callMergeSort)
        algoritmMenu.add_command(label='Heap sort',command=self.callHeapSort)
        self.count=0
        # time.sleep(.5)
        # print("test")
        self.app.mainloop()




if __name__ == "__main__":
    # m = ThemedTk(theme='radiance')
    m=Tk()
    # m = tk.ThemedTk()
    # m.get_themes()                 # Returns a list of all themes that can be set
    # m.set_theme("arc")  
    # ttk.Style().theme_use('clam')
    m.title("Algoritam Visualizer")
    w =  Canvas(m,width=100,height=100)
    w.config(width=w.winfo_screenwidth(), height=w.winfo_screenheight())
    w.pack()
    m.geometry("%dx%d" % (w.winfo_screenwidth(), w.winfo_screenheight()))
    app=App(w,m)
    app.mainFunction()