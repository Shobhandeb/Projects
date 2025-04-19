from tkinter import *
from PIL import Image, ImageTk
habbit_root = Tk()

#giving the size of window 
#"widthxheight"
habbit_root.geometry("644x434")
#setting min size
# width,height 
habbit_root.minsize(300,300)
# habbit_root.maxsize(900,900)


#tkinter support png files only 
# photo = PhotoImage(file="math assignment 2.png")
# #labeling the photo 
# photoLabel = Label(image=photo)
# photoLabel.pack()

#for jpeg file image we need to import Image and ImageTk from PIL

image = Image.open("maya.jpeg")
photo = ImageTk.PhotoImage(image)

photoLabel = Label(image=photo)
photoLabel.pack()
#label : the part of gui which has no user side use 
# label1=Label(text="Hi , this is my first tkinter GUI application")
# label1.pack()
habbit_root.mainloop()
