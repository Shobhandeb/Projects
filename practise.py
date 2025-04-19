from tkinter import *

def hi():
    print("Hello")
base_root = Tk()
base_root.geometry("666x400")
base_root.title("Menubar")



m1 = Menu(base_root)
#for packing 
base_root.config(menu = m1)



m1.add_cascade(label="first menu item " , command=hi )

#now dropdown menu 

m2 = Menu(m1)
m2.add_command(label = "File" , command=hi)
m2.add_command(label = "Save As" , command=hi)
m2.add_command(label="Edit" , command=hi)

m1.add_cascade(label="Dropdown Menu" , menu=m2)




base_root.mainloop()