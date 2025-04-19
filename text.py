from tkinter import *

my_app = Tk()
my_app.geometry("500x400")
photo = PhotoImage(file="label.png")
photoLabel = Label(image=photo)

# text = Label(text="Hi i am a disciplined men who is consistent about his habit \n I am a topper and i will be a topper agian " , 
            #  bg = "red" ,fg="white",padx=112,pady=113,font="comicsansms 19 bold", borderwidth=5,relief=GROOVE)
text = Label(text="Ready", bg="red" ,fg="white")
text.pack(side="bottom" ,pady=3,fill=X )
photoLabel.pack( anchor="sw" ,pady=0)
#side = top , bottom , left , right 
my_app.mainloop()

#7 to start
