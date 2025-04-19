
#declaring variable 
# values = 0
# result = 0 
from tkinter import *
#importing time module :
import time
#gui interface 
root = Tk()
root.geometry("392x680")
root.wm_iconbitmap("calc.ico")
root.title("Calculator")
scvalue = StringVar()
scvalue.set("")

def click(event):
    text = event.widget.cget("text")
    # print(text)
    global values 
    global result
    #main line
    if text == "=":
        if scvalue.get().isdigit():
            values = scvalue.get()
            # result = float(scvalue.get())
            scvalue.set(values)
            screen.update()

        else:
            values = scvalue.get()
            try:
                result = eval(values)
                scvalue.set(float(result))
                screen.update
            except Exception as e :
                scvalue.set("Error")
                screen.update
    elif text == "AC":
        values = 0 
        result = 0
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

#designing part 
screen = Entry(root, textvariable= scvalue , font= "Helvetica 38 bold" )
screen.pack(fill=X , ipadx=12 , ipady= 12 , padx=12 , pady=12)

#creating a frame and adding button 
frame1 = Frame(root, background="grey" ,pady=7)

button1 = Button(frame1 , text= "1"  , padx=12.5 , font="lucida 32 bold" ,width=2, relief=RAISED ,bd = 7 )
button1.pack(side="left" , padx=10 , pady=7)
button1.bind("<Button-1>" , click)


button2 = Button(frame1 , text= "2"  , padx=12.5, font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button2.pack(side="left" , padx=10 , pady=7)
button2.bind("<Button-1>" , click)

button3 = Button(frame1 , text= "3"  ,padx=12.5 , font="lucida 32 bold" ,width=2, relief=RAISED ,bd = 7)
button3.pack(side="left" , padx=10 , pady=7)
button3.bind("<Button-1>" , click)

frame1.pack()

#creating a frame and adding button 
frame2 = Frame(root, background="grey")

button4 = Button(frame2 , text= "4"  , padx=12.5 , font="lucida 32 bold" ,width=2, relief=RAISED ,bd = 7)
button4.pack(side="left" , padx=10 , pady=7)
button4.bind("<Button-1>" , click)


button5 = Button(frame2 , text= "5"  ,padx=12.5, font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button5.pack(side="left" , padx=10 , pady=7)
button5.bind("<Button-1>" , click)

button6 = Button(frame2 , text= "6"  , padx=12.5 , font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button6.pack(side="left" , padx=10 , pady=7)
button6.bind("<Button-1>" , click)

frame2.pack()
#creating a frame and adding button 
frame3 = Frame(root, background="grey")

button7 = Button(frame3 , text= "7"  ,padx= 12.5 , font="lucida 32 bold" ,width=2, relief=RAISED ,bd = 7)
button7.pack(side="left" , padx=10 , pady=7)
button7.bind("<Button-1>" , click)


button8 = Button(frame3 , text= "8"  , padx=12.5, font="lucida 32 bold",width=2 , relief=RAISED,bd = 7)
button8.pack(side="left" , padx=10 , pady=7)
button8.bind("<Button-1>" , click)

button9 = Button(frame3 , text= "9"  , padx=12.5, font="lucida 32 bold",width=2 , relief=RAISED,bd = 7)
button9.pack(side="left" , padx=10 , pady=7)
button9.bind("<Button-1>" , click)

frame3.pack()

#creating a frame and adding button  + , -  , * , / , ^ , % 
frame4 = Frame(root, background="grey" , pady=5)

button10 = Button(frame4 , text= "+"  ,padx=12.5 , font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button10.pack(side="left" , padx=10 , pady=7)
button10.bind("<Button-1>" ,click )


button11 = Button(frame4 , text= "-"  , padx=12.5 , font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button11.pack(side="left" , padx=10 , pady=7)
button11.bind("<Button-1>"  , click)

button12 = Button(frame4 , text= "*"  ,padx= 12.5 , font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button12.pack(side="left" , padx=10 , pady=7)
button12.bind("<Button-1>"  , click)

frame4.pack()

#creating a frame and adding button 
frame5 = Frame(root, background="grey")

button13 = Button(frame5 , text= "AC"  , padx=12.5 , font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button13.pack(side="left" , padx=10 , pady=7)
button13.bind("<Button-1>"   , click)


button14 = Button(frame5 , text= "/"  , padx=12.5 , font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button14.pack(side="left" , padx=10 , pady=7)
button14.bind("<Button-1>" , click)

button15 = Button(frame5 , text= "="  ,padx=12.5 ,font="lucida 32 bold",width=2 , relief=RAISED ,bd = 7)
button15.pack(side="left" , padx=10 , pady=7)
button15.bind("<Button-1>" ,click)

frame5.pack()
root.mainloop()