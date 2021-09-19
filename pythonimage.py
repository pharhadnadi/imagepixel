#Farhad Nadi 2019
from PIL import Image
import numpy as np
 
import argparse

# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-i", "--image", required=True, help="input image")
args = vars(ap.parse_args())




numofpixels = 6 #there are 6 .png files named from 1 to 6
chunklen = 5


imgname =args['image']
img = Image.open(imgname).convert('LA')
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
       newpix = Image.open('pixeldb\\'+str(numofpixels-(int(chuncksum/(255/numofpixels))+1))+'.png')
       

       newim.paste(newpix.resize((chunklen, chunklen), Image.ANTIALIAS), (row,col))

# newim.show()
newim.save(imgname.split('.')[0]+'out.png')
