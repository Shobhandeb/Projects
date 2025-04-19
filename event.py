from tkinter import * 

def show(event):
    print(f"The location of mouse pointer in x =  {show} and y = {show}")

root = Tk()
root.title("Events")
root.geometry("600x300")

button = Button(root, text="Click On Me")
button.pack()
button.bind('<Button-1>' ,show)
button.bind('<Double-1>' , quit)
root.mainloop()