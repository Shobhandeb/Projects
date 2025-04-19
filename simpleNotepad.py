from tkinter import * 
root = Tk()
root.geometry("400x200")
root.title("Simple Notepad")

scroll_bar = Scrollbar(root)
scroll_bar.pack(fill=Y,side="right")

text = Text(root , width=1200, height=900,yscrollcommand=scroll_bar.set)
text.pack(pady=3)

scroll_bar.config(command=text.yview)



root.mainloop()