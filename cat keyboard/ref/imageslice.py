from PIL import Image
import matplotlib.pyplot as plt

img=Image.open('hands_left.jpg')

small_img=img.resize((128*2,128*2),Image.BILINEAR)


#show image
o_size=(128*2,128*2) #output size
res=small_img.resize(o_size,Image.NEAREST)
#save image
res.save('hands_left1.jpg')
#display image
plt.imshow(res)
plt.show()