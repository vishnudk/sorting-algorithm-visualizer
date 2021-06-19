
from tkinter import *
import random
import time
class app:
    def __init__(self,app,canvas):
        self.app=app
        self.canvas=canvas
        # self.aSize=

    def createRandomArrayList():
        aSize=(arraySize.get())
        l=[]
        for i in range(aSize):
            l.append(random.randint(100,200))
        self.arraySizeSelector()
        # return l
    def arraySizeSelector():
        aSize=(self.canvas.arraySize.get())
        x=(int(canvas.winfo_screenmmwidth()/2)-((aSize/2)*10))+550
        line=[]
        for i in range(aSize):
            line.append(canvas.create_line(x+(i*10),l[i], x+(i*10), 100))
        # for i in line:
            # print(w.coords(i))
        # time.sleep(3)
        # for i in range(len(l)-1):
        #     index=i
        #     posTmp=pos=w.coords(line[i])
        #     for j in range(i+1,len(l)):
        #         if l[j]<l[index]:
        #             posTmp=w.coords(line[j]) 
        #             index=j
        #     tmp=l[index]
        #     l[index]=l[i]
        #     l[i]=tmp
        #     tmp=pos
        #     pos=posTmp
        #     posTmp=tmp
        #     w.move(line[i],pos)
        #     w.move(line[index],posTmp)

        
        # pass
def function():
    m = Tk()
    root=m
    m.title("Algoritam Visualizer")
    w =  Canvas(m,width=100,height=100)
    w.config(width=w.winfo_screenwidth(), height=w.winfo_screenheight())
    w.pack()
    aSize=0
    appO=app(m,w)
    m.geometry("%dx%d" % (w.winfo_screenwidth(), w.winfo_screenheight()))
    # print(w.winfo_screenwidth())
    l=Label(m, text = "Array Size") 
    l.place(x=0,y=10)
    arraySize = Scale(m, from_=0, to=140, orient=HORIZONTAL)
    arraySize.place(x=80,y=0) 
    button = Button(m, text='create', width=10, command=arraySizeSelector)
    button.place(x=200,y=10)

    menu = Menu(root) 
    root.config(menu=menu) 
    filemenu = Menu(menu) 
    menu.add_cascade(label='File', menu=filemenu) 
    filemenu.add_command(label='New') 
    filemenu.add_command(label='Open...') 
    # filemenu.add_separator() 
    filemenu.add_command(label='Exit', command=root.quit) 
    helpmenu = Menu(menu) 
    menu.add_cascade(label='Help', menu=helpmenu) 
    helpmenu.add_command(label='About',command=createRandomArrayList) 
    algoritmMenu=Menu(menu)
    menu.add_cascade(label='Algorithms',menu=algoritmMenu)
    algoritmMenu.add_command(label='Buble sort')
    algoritmMenu.add_command(label='Quick sort')
    algoritmMenu.add_command(label='Merge sort')
    algoritmMenu.add_command(label='Selection sort')
    y=10
        
    m.mainloop()

if __name__ == "__main__":
    function()