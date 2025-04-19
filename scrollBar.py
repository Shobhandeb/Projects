from tkinter import * 

root = Tk()
root.geometry ("500x400")
root.title("Scrolling through list ")
i = 1
def add():
    global i
    list_box.insert(END,f"{i}")
    i +=1
#rules for adding any scrollbar : 

#first create a varible scrollbar and pack it for adding in right give side = "right " and fill = Y
# WidgetName(yscrollcommand = scrollbar.set)
#scrollbar.config(command = WidgetName.yview)

#creating scrool bar : 

scrollbar = Scrollbar(root)
scrollbar.pack(side= "right", fill=Y)


list_box = Listbox(root , width=50 , yscrollcommand=scrollbar.set)
list_box.pack()

scrollbar.config(command=list_box.yview)

list_box.insert(ACTIVE,0)



Button(root,text="Add Items" , background="red" , command=add).pack()

root.mainloop()


#start from lecture #22 from 5 minutes 