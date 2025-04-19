from tkinter import * 
import tkinter.messagebox as t

def show():
    print("There is a response , hack it ! ")
    t.showinfo("Congratulation ! " , f"wow ! ${slider.get()} amount will be credited to your bank account very soon ")
    a = t.askokcancel("Go" , "Click Ok to Receive the money ")
    if a == True:
        quit()
    else : 
        t.showerror("Cancelled " , "Opss better luck next time , you haven't followed our instruction properly , it's your mistake , you lost the golden opportunity of wining the money ")
    print("\n All Details have been received ")


root = Tk()
root.geometry("666x444")
root.title("You get a lottery ")
Label(root,text="How much dollar you want ? " , font="Arial" , pady=20).pack()

slider = Scale(root, from_=0, to=100, length=200, orient=HORIZONTAL , tickinterval=25)
slider.pack()

Button(root, text="Get Dollar ", command=show).pack()


root.mainloop()



