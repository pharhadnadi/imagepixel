from PIL import Image
import numpy as np
 
img = Image.open('lady0.jpg').convert('LA')
#pix = img.load()

img.show()
width, height = img.size

newim = Image.new("RGB", (width, height), "white")

chunklen = 5

for row in range(0,width, chunklen):
    
    for col in range(0, height, chunklen):        
       chuncksum=0
    #    print(row, col)
       for rowchunck in range(1,chunklen):            
           for colchunck in range(1,chunklen):        
            #    print('(',row+rowchunck , col+colchunck,')', end=',')
               
               if (row+rowchunck<width and col+colchunck<height):
                   chuncksum += img.getpixel((row+rowchunck, col+colchunck))[0]
       chuncksum/=(chunklen**2)
       newpix = Image.open(str(6-(int(chuncksum/42.5)+1))+'.png')
       

       newim.paste(newpix.resize((chunklen, chunklen), Image.ANTIALIAS), (row,col))

newim.show()
