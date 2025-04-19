#to create a file  using makedirs()

import os
#creating a folder 
def createIfNotExits(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    

#finding files 
files = os.listdir()
files.remove("fileCleaner.py")

#extensions
imgExts = [".png" ,".jpg" ,".jpeg"]
docExts =[".txt",".pdf" , ".docx" , ".doc"]
mediExts = [".mp4" ,".mp3" , ".flv"]
createIfNotExits('Image')
createIfNotExits('Docs')
createIfNotExits('Media')
createIfNotExits('Others')

imageLists = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]
docLists = [file for file in files if os.path.splitext(file)[1].lower() in docExts ]
mediaLists = [file for file in files if os.path.splitext(file)[1].lower() in mediExts ]

otherList = []

for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        otherList.append(file)


#creting function :
def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

print(mediaLists)
#moving files to respective folders : 

move('Media',mediaLists)
move('Others',otherList)
move('Docs',docLists)
move('Image',imageLists)
# for media in mediaLists:
#     os.replace(media,f"Media/{media}")
# for media in docLists:
#     os.replace(media,f"Docs/{media}")
# for media in imageLists:
#     os.replace(media,f"Image/{media}")
# for media in otherList:
#     os.replace(media,f"Others/{media}")

#printing 
# print(imageLists)
# print(docLists)
# print(mediaLists)
print(otherList)




