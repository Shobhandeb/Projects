from tkinter import * 

def values():
    print("\n")
    print(f"The name of the person is {nameValue.get()}")
    print(f"The name of the person is {phoneValue.get()}")
    print(f"The name of the person is {genderValue.get()}")
    print(f"The name of the person is {emergencyphoneValue.get()}")
    print(f"The name of the person is {payValue.get()}")
    x = foodservice.get()
    if(x==0):
        print("No prebooking is done ")
    else:
        print("Prebooking  is done ")
    
    print("\n The form is submitted succesfully , We will contact you soon ! ")


root = Tk()
root.geometry("625x400")
Label(root, text= "  Name  ").grid(row=0, column=1)
Label(root, text= "  Phone  ").grid(row=1, column=1)
Label(root, text= "  Gender ").grid(row=2, column=1)
Label(root, text= "  Emergency Contact ").grid(row=3, column=1)
Label(root, text= "  Payment    Mode  ").grid(row=4, column=1)

nameValue = StringVar()
phoneValue = IntVar()
genderValue = StringVar()
emergencyphoneValue = IntVar()
payValue = StringVar()
foodservice = IntVar()



name = Entry(root, textvariable=nameValue).grid(row=0, column=3)
phone = Entry(root, textvariable=phoneValue).grid(row=1, column=3)
gender = Entry(root, textvariable=genderValue).grid(row=2, column=3)
emph = Entry(root, textvariable=emergencyphoneValue).grid(row=3, column=3)
pay = Entry(root, textvariable=payValue).grid(row=4, column=3)


Checkbutton(text= "want to prebook your meals" , variable = foodservice).grid(row=5,column=2)

Button(root, text="Submit" ,bg="red" ,command=values ).grid(row=6,column=3)


root.mainloop()



