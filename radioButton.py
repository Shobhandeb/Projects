from tkinter import * 
import tkinter.messagebox as t

def order():
    t.showinfo("Confirmation" , f"Your order for {a.get()}  is ready , Confirm it for Delivery .")

root =Tk()
root.geometry("444x400")
root.title("Omato")

#variable 
a = StringVar()
a.set("NOne")

Label(root,text="What would you like for having in the lunch" , font="lucida 14 bold").pack()
radio = Radiobutton(root, text="Chili Chicken " ,variable=a, value="Chili Chiken" , padx=40, pady=20).pack(anchor="w")
radio = Radiobutton(root, text="Chicken kemma" , variable=a,value="Chicken kemma " , padx=40, pady=20).pack(anchor="w")
radio = Radiobutton(root, text="Biriyani" ,variable=a, value="Biriyani" , padx=40, pady=20).pack(anchor="w")
radio = Radiobutton(root, text="Fried Chicken rice " ,variable=a, value="Fried Chicken rice" , padx=40, pady=20).pack(anchor="w")
radio = Radiobutton(root, text="Chili Chicken combo  " ,variable=a, value="Chili Chicken combo " , padx=40, pady=20).pack(anchor="w")
Button(text="Confirmed Order" , command=order).pack()

root.mainloop()