from tkinter import * 

import tkinter.messagebox as tmsg
def helpMe():
    print("Help me ")
    a = tmsg.showerror("Help" , "under development ! ")
    print(a)
def contactUs():
    print("WE will contact you soon ")
    response = tmsg.askquestion("Rate us " , "Was your experience with our gui Good ? ")
    if response == "yes":
        tmsg.askokcancel("Rate us "  , "Rate us the app store ")
    else : 
        tmsg.showerror("sorry " , "We will take your matter to our experts , don't worry ")
    



root = Tk()
root.geometry("666x444")
root.title("Messege Box")

m1 = Menu(root)
root.config(menu=m1)
drop_menu = Menu(m1, tearoff=0)
drop_menu.add_command(label="Help" , command=helpMe)
drop_menu.add_command(label="Contact Us " , command =contactUs)

m1.add_cascade(label="Help" , menu=drop_menu)

root.mainloop()