from tkinter import * 
root = Tk()

canvaWidth = 700
canvaHeight = 400

root.geometry(f"{canvaWidth}x{canvaHeight}")

canwidget = Canvas(root, width= canvaWidth , height= canvaHeight)
canwidget.pack()
#The line goes form x1 , y1 to x2 , y2 
canwidget.create_line(100,10 , canvaWidth-150, 10 , fill="red" )
canwidget.create_line(100,40 , canvaWidth-150, 40  , fill= "red")

canwidget.create_rectangle(250,15, 350 , 36 , fill="red")

canwidget.create_text(300,30, text="OVAL" ,fill="white"  , font="SansSerif")
canwidget.create_oval(200,50 , 400,150 ,fill="blue")


root.mainloop()



#14 theke start 