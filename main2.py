
from tkinter import *
import random
import time
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
    def sort(self):
         pass   
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
               
            if   self.array[self.prvJ]<=self.array[self.pivot] : 
                self.prvJ=self.prvJ-1 
                self.canvas.move(self.CheckLine2,-10,0)
                self.flag=2
                self.canvas.after( 20-int(self.searchSpeed))
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
               
           
       
        self.array[self.prvJ],self.array[self.pivot]=self.array[self.pivot],self.array[self.prvJ]
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
            self.QickSort(tmpPivot,tmpJ-1)
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
            self.QickSort(tmpJ+1,tmpEnd) 
    
            

        


    def CallQuicksort(self):
        self.QickSort(0,self.arrayLength-1)
        try:
            self.canvas.delete(self.CheckLine1)
            # self.canvas.delete(self.CheckLine2)
        except:
            pass
        try:
            # self.canvas.delete(self.CheckLine1)
            self.canvas.delete(self.CheckLine2)
        except:
            pass
        
        # self.printArray()
    def bubbleSort(self):
        if self.count==0:
            self.count=1
            self.prvI=self.prvI+1
            self.CheckLine = self.canvas.create_line(self.canvas.coords(self.line[0])[0],max(self.array),self.canvas.coords(self.line[0])[2],self.canvas.coords(self.line[0])[3],width=10,fill='green')
        while self.prvI<self.arrayLength-1:
            while self.prvJ<self.arrayLength-1-self.prvI:
                # self.canvas.move
                if self.flag==0:
                    self.canvas.move(self.CheckLine,10,0)
                    self.flag=1
                    break
                if self.flag==1:
                    self.canvas.move(self.CheckLine,-10,0)
                    self.flag=2
                    break
                self.flag=0
                self.canvas.move(self.CheckLine,10,0)
                if self.array[self.prvJ]<self.array[self.prvJ+1]:
                    self.array[self.prvJ],self.array[self.prvJ+1]=self.array[self.prvJ+1],self.array[self.prvJ]
                    self.canvas.move(self.line[self.prvJ],10,0)
                    self.canvas.move(self.line[self.prvJ+1],-10,0)
                    self.line[self.prvJ],self.line[self.prvJ+1]=self.line[self.prvJ+1],self.line[self.prvJ]
                self.prvJ=self.prvJ+1
                break
            if self.prvJ>=self.arrayLength-1-self.prvI:
                self.canvas.delete(self.CheckLine)
                self.CheckLine = self.canvas.create_line(self.canvas.coords(self.line[0])[0],max(self.array),self.canvas.coords(self.line[0])[2],self.canvas.coords(self.line[0])[3],width=10,fill='green')
                self.canvas.itemconfig(self.line[self.arrayLength-1-self.prvI],fill='blue')
                self.prvI=self.prvI+1
                self.prvJ=0
            break
        if self.flag==0:
            self.canvas.after(20-int(self.searchSpeed),self.bubbleSort)
        elif self.prvI<self.arrayLength-1:
            self.canvas.after(100-int(self.searchSpeed),self.bubbleSort)
        else:
            self.canvas.itemconfig(self.line[0],fill='blue')
            self.canvas.delete(self.CheckLine)
            # print (self.array)
            self.CheckLine=-1
            self.coords=[]
            self.index=1
            self.max=-1
            self.pos = 0
            self.prvI=-1
            self.prvJ=1
            self.count=0
            self.maxPos=0
       
    
    def selectionSort(self):
     
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
            self.canvas.after(20-int(self.searchSpeed),self.selectionSort)
        else:
            self.canvas.delete(self.CheckLine)
            # print (self.array)
            self.CheckLine=-1
            self.coords=[]
            self.index=1
            self.max=-1
            self.pos = 0
            self.prvI=-1
            self.prvJ=1
            self.count=0
            self.maxPos=0
     
      
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
        algoritmMenu.add_command(label='Buble sort',command=self.bubbleSort)
        algoritmMenu.add_command(label='Quick sort',command=self.CallQuicksort)
        algoritmMenu.add_command(label='Merge sort',command=self.sort)
        algoritmMenu.add_command(label='Selection sort',command=self.selectionSort)
        self.count=0
        # time.sleep(.5)
        # print("test")
        self.app.mainloop()




if __name__ == "__main__":
    m = Tk()
    m.title("Algoritam Visualizer")
    w =  Canvas(m,width=100,height=100)
    w.config(width=w.winfo_screenwidth(), height=w.winfo_screenheight())
    w.pack()
    m.geometry("%dx%d" % (w.winfo_screenwidth(), w.winfo_screenheight()))
    app=App(w,m)
    app.mainFunction()