from tkinter import *

# biography

root = Tk()
root.title("FaceBook")

root.geometry("1300x700")
photoFrame = Frame(root, width=80, height=80, bd=5,
                   relief="groove", padx=30, pady=20)

textFrame =  Frame(root, bd=5, relief="ridge", padx=25,
                  pady=25, bg="blue", width=80, height=500)

text = Label(textFrame, text='''Facebook is an online social 
             media and social networking service owned by American 
             technology giant Meta Platforms. Created in 2004 by 
             Mark Zuckerberg with fellow Harvard College students
              and roommates Eduardo Saverin, Andrew McCollum, 
             Dustin Moskovitz, and Chris Hughes, its name derives
              from the face book directories 
             often given to American university students.''', padx=10, pady=10, bg="red", fg="white" , font=("Helvetica" , 24))

# photoFrame.place(x=1,y=1)
photo = PhotoImage(file="smallimage.png")
imgLabel = Label(photoFrame, image=photo)
# placing frame
photoFrame.place(x=20, y=250)
textFrame.place(x=230, y=250)

text.pack(side="top")

imgLabel.pack()


root.mainloop()
