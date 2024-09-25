from PIL import Image
import os

i = Image.open("i1.jpg")

w,h=i.size
print(w,h)



#i = i.crop((0,0,(w/2),(h/2)))

#i.save("newi1.jpg")