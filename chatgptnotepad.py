from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
import os

def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    textArea.delete(1.0, END)

def openfile():
    global file
    file = askopenfile(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file is None:
        return
    root.title(os.path.basename(file.name) + " - Notepad")
    textArea.delete(1.0, END)
    content = file.read()
    textArea.insert(1.0, content)
    file.close()

def savefile():
    global file
    if file is None:
        file = asksaveasfile(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file is None:
            return
    content = textArea.get(1.0, END)
    file.write(content)
    file.close()

def cut():
    textArea.event_generate("<<Cut>>")

def copy():
    textArea.event_generate("<<Copy>>")

def paste():
    textArea.event_generate("<<Paste>>")

def about():
    print("Notepad by code with harrry")

def quitApp():
    root.destroy()

if __name__ == "__main__":
    root = Tk()
    root.title("Untitled - Notepad")
    root.geometry("644x700")
    # Change this line to the path of your icon file
    root.iconbitmap("notepad.ico")

    textArea = Text(root, font="lucida 15")
    textArea.pack(expand=True, fill=BOTH)

    file = None

    menuBar = Menu(root)

    fileMenu = Menu(menuBar, tearoff=0)
    fileMenu.add_command(label="New", command=newfile)
    fileMenu.add_command(label="Open", command=openfile)
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    menuBar.add_cascade(label="File", menu=fileMenu)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    menuBar.add_cascade(label="About us", menu=helpMenu)

    root.config(menu=menuBar)

    scroll = Scrollbar(textArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)

    root.mainloop()
