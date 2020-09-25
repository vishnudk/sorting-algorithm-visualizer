
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
        self.coords=[]
        # self.sort=0
        self.count=0
    def sort(self):
        # self.sort=1
        # count=0
        # print(self.array)
        for i in range(self.arrayLength-1):
            pos=i
            max=self.array[i]
            for j in range(i+1,self.arrayLength):
                # if self.count==1:
                    # self.printArray()
                if max<self.array[j]:
                    max=self.array[j]
                    pos=j
                        # self.printArray()
                    # self.count=0
            tmp = self.array[i]
            self.array[i]=self.array[pos]
            self.array[pos]=tmp
            # time.sleep(.2)
            # self.printArray()
        self.printArray()
        # print(self.array)
        # self.createRandomArray()
            # self.canvas.move(self.line[pos],-count,0)
            # tmp=self.coords[i]
            # self.coords[i]=self.coords[pos]
            # self.coords[pos]=tmp
            # tmp=self.line[pos]
            # self.line[pos]=self.line[i]
            # self.line[i]=tmp
           
            # self.canvas.coords(self.line[i],maxValCoord[0],maxValCoord[1],maxValCoord[2],maxValCoord[3])
            # self.canvas.coords(self.line[pos],intiCoord[0],intiCoord[1],intiCoord[2],intiCoord[3])
            # self.printArray()
            # self.printArray()
            # time.sleep(.25)
        # print(self.coords)
        # self.printArray()
        # print("==================")
        # print(self.coords)
        

    def printArray(self):
        self.canvas.delete("all")
        x=(int(self.canvas.winfo_screenmmwidth()/2)-((self.arrayLength/2)*10))+550
        for i in range(self.arrayLength):
            self.line.append(self.canvas.create_line(x+(i*10),self.array[i], x+(i*10), 100))
            self.coords.append([x+(i*10),self.array[i], x+(i*10), 100])
    def createRandomArray(self):
        self.canvas.delete("all")
        self.array=[]
        self.line=[]
        self.arrayLength=self.arraySize.get()
        for i in range(self.arrayLength):
            self.array.append(random.randint(100,100+self.arrayLength))
        # print(self.array)
        x=(int(self.canvas.winfo_screenmmwidth()/2)-((self.arrayLength/2)*10))+550

        for i in range(self.arrayLength):
            self.line.append(self.canvas.create_line(x+(i*10),self.array[i], x+(i*10), 100))
            self.coords.append([x+(i*10),self.array[i], x+(i*10), 100])
        # print(self.line)
        # self.printArray()
        # print(self.coords)
    
    def mainFunction(self):
        # array selection region
        l=Label(self.app, text = "Array Size") 
        l.place(x=0,y=10)
        self.arraySize = Scale(self.app, from_=0, to=140, orient=HORIZONTAL)
        self.arraySize.place(x=80,y=0) 

        button = Button(self.app, text='create', width=10, command=self.createRandomArray)
        button.place(x=200,y=10)
        
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
        algoritmMenu.add_command(label='Buble sort',command=self.sort)
        algoritmMenu.add_command(label='Quick sort',command=self.sort)
        algoritmMenu.add_command(label='Merge sort',command=self.sort)
        algoritmMenu.add_command(label='Selection sort',command=self.sort)
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