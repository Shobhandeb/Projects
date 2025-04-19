from tkinter import *

root = Tk()
root.geometry("666x400")
root.title("MenuBar")

def hello():
    print(" Hello World !")
    Label(root, text="Hellow World ! " , font="comicsans 23" ).pack(anchor="w" , side="left")

#single menu 
# m1 = Menu(root)

#helps in adding menu :
# root.config(menu=m1)

# m1.add_command(label = "File" , command=hello)
# m1.add_command(label = "Edit" , command=hello)
# m1.add_command(label = "Selection" , command=hello)
# m1.add_command(label = "View" , command=hello)
# m1.add_command(label = "Go" , command=hello)



#dropdown menus * 

m1 = Menu(root)
root.config(menu=m1)
m1.add_cascade(label="hi")

drop_m1 = Menu(m1 , tearoff=0)
drop_m1.add_command(label = "File" , command=hello)
drop_m1.add_command(label = "New File" , command=hello)
drop_m1.add_separator()
drop_m1.add_command(label = "Save" , command=hello)
drop_m1.add_command(label = "Save As" , command=hello)
drop_m1.add_separator()
drop_m1.add_command(label = "View" , command=hello)
drop_m1.add_command(label = "Edit" , command=hello)
#final giving the tittle of dropdown 
m1.add_cascade(label="Selection" , menu=drop_m1)


root.mainloop()