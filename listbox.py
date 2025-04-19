from tkinter import * 
import tkinter.messagebox as t

def add():
    global i
    list_box.insert(END,f"{i}")
    i +=1

i = 1
root = Tk()
root.title("ListBox")
root.geometry ("500x400")

list_box = Listbox(root , width=50)
list_box.pack()

list_box.insert(ACTIVE,0)

Button(root,text="Add Items" , background="red" , command=add).pack()


root.mainloop()