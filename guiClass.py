from tkinter import * 

#importing tk as a gui class
class GUI(Tk):
    #defining a construction 
    def __init__(self):
        super().__init__()
        self.geometry ("744x377")

    #creating a status bar by function 
    def status(self):
        self.var = StringVar()
        self.var.set("Ready")
        self.statusvar = Label(self,textvariable=self.var , relief=SUNKEN,anchor="w")
        self.statusvar.pack(fill=X , side=BOTTOM)
    
    #def creating click function 
    def click(self):
        print("Button is Clicked ")

    def do(self):
        Button(text="Hi" , command= self.click , anchor="e").pack(side=RIGHT)

    #creating a button 
    def createButton(self,imptext):
        Button(text= imptext , command= self.do , anchor="w").pack(side=LEFT)


class hi(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("900x200")

        Label(text="Happy Independence Day" , relief=RIDGE , anchor=CENTER).pack(fill=X , side =BOTTOM)



if __name__ =='__main__':
    window = GUI()
    window.status()
    window.createButton("hello")
    
    window.mainloop()

    window2 = hi()
    window2.mainloop()
                 












