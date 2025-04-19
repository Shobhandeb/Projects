from tkinter import *
from PIL import ImageTk , Image

#import data and time 



#breaking line
def lineBreak(text):
    final_text = ""
    for i in range(0,len(text)):
        final_text += text[i]
        if i%92 ==0 and i!= 0 :
            final_text += "\n"
    
    return final_text





root = Tk()
root.title("Daily News")
root.geometry("1000x700")


text = []

photo = []

for i in range(0,3):
    with open(f"{i+1}.txt" , encoding= 'utf-8') as f:
        texts = f.read()
        text.append(texts)
    image = Image.open(f"{i+1}.png")
    #resize of the images
    image = image.resize((200,200),Image.ANTIALIAS)
    #appending image
    photo.append(ImageTk.PhotoImage(image))


#creating and frames and main thing starts : 
f0 = Frame(root, width=700 , height= 300 )
f0.pack()
Label(f0,text="News By Daily News" , font="lucida 32 bold").pack()
can =Canvas(f0 ,width=800 , height=10 )
can.pack()
can.create_line(90,10 , 710 , 10 , fill="red")
#first frame
f1 = Frame(root, width=600 , height = 400)
f1.pack(anchor="w" , padx=17, pady=15)
Label(f1, text=lineBreak(text[0]), font ="Arial 10 " , padx=10 , pady=10).pack(side="left")
Label(f1, image=photo[0] ).pack()
#2nd frame
f2 = Frame(root, width=600 , height = 400)
f2.pack(anchor="w" , padx=19, pady=5)
Label(f2, text=lineBreak(text[1]), font ="Arial 10 " , padx=10 , pady=10).pack(side="right")
Label(f2, image=photo[1] ).pack(side="left")
#3rd frame 
f3 = Frame(root, width=600 , height = 400)
f3.pack(anchor="w" , padx=19, pady=5)
Label(f3, text=lineBreak(text[2]), font ="Arial 10 " , padx=10 , pady=10).pack(side="left")
Label(f3, image=photo[2] ).pack(side="right")





# f1= Frame(root , width= )

root.mainloop()