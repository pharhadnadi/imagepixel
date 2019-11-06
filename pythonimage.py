#Farhad Nadi 2019
from PIL import Image
import numpy as np
 

numofpixels = 6 #there are 6 .png files named from 1 to 6
chunklen = 5



img = Image.open('lady0.jpg').convert('LA')
#pix = img.load()

img.show()
width, height = img.size

newim = Image.new("RGB", (width, height), "white")



for row in range(0,width, chunklen):
    
    for col in range(0, height, chunklen):        
       chuncksum=0    
       
       for rowchunck in range(1,chunklen):            
           for colchunck in range(1,chunklen):                       
               if (row+rowchunck<width and col+colchunck<height):
                   chuncksum += img.getpixel((row+rowchunck, col+colchunck))[0]
       chuncksum/=(chunklen**2)
       newpix = Image.open(str(numofpixels-(int(chuncksum/(255/numofpixels))+1))+'.png')
       

       newim.paste(newpix.resize((chunklen, chunklen), Image.ANTIALIAS), (row,col))

newim.show()
