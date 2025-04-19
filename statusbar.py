from tkinter import * 

def update():
    statusvar.set("uploading")
    status.update()
    import time
    time.sleep(4)
    statusvar.set("Submitted successfully !")



root = Tk()
root.title("Status Bar")
root.geometry("500x300")

statusvar = StringVar()
statusvar.set("Ready ....")
status = Label(root, textvariable= statusvar , relief= SUNKEN , anchor="w")
status.pack(side= BOTTOM , fill= X)
Button(root, text="submit" ,command=update).pack()

root.mainloop()