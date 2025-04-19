from tkinter import * 

root = Tk()
root.geometry("644x444")
root.title("Tkinter project ")
root.wm_iconbitmap("icon.ico")

root.configure(background="grey")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"The size of my pc screen is {width}x{height}")

Button(text="Close" ,command=root.destroy , padx=20 , pady = 20 ).pack(side=BOTTOM)
root.mainloop()