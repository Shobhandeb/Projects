from tkinter import * 

def resize():
    root.geometry(f"{width.get()}x{height.get()}")
    print("Updating gui ")


root = Tk()
root.geometry("400x200")
root.title("Resize window ")

Label(root,text="Give the width ").pack()

width = StringVar()
height = StringVar()
Entry(root , width=30, textvariable=width).pack()

Label(root,text="Give the height ").pack()

Entry(root , width= 30 , textvariable=height).pack()

Button(root , text= "Apply Now" , command= resize).pack()

root.mainloop()


#24 is completed but not practise , start from 25 