from tkinter import * 

def getVals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of passsword is {passvalue.get()}")


root = Tk()
root.geometry("745x600")

user = Label(root,text="username")
password = Label(root, text="Password")

#packing with grid 
user.grid(row = 0 , column = 0 )
password.grid(row = 1 , column=0)

#variable classes in Tkinter 
#BooleanVar , DoubleVar , IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
userentry.grid(row=0 , column=1)

passentry = Entry (root,textvariable= passvalue , show="*" )
passentry.grid(row = 1,column=1 )

Button(text="Submit" , command=getVals) .grid(row=3, column = 1)

root.mainloop()