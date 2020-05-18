import sys
import os 
from PIL import Image 
 
"""
This file is self-contained and allows the user to give 
an input of image files in the .jpg extension and convert
them to .png

The must give two inputs when running this file. THe first 
is the file that contains the images, while the second is the 
desired name of the new folder. The folder does not have to
exist as the program will create it. 
"""

#Get path to arguement folders
current_pics = sys.argv[1]
new_pics = sys.argv[2]

#Create new_pics path if it doesn't exist
if not os.path.exists(new_pics):
	os.makedirs(new_pics)

#Go through each image and change file extension from .jpg to .png
for imagename in os.listdir(current_pics):
	img = Image.open(f'{current_pics}{imagename}')
	split_name = os.path.splitext(imagename)[0]		#split the name of the image from .jpg extension
	img.save(f'{new_pics}{split_name}.png', 'png')	#add .png extension to the name

print ('all done!')