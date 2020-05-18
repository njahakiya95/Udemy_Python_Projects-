import sys
import os 
from PIL import Image 
 

current_pics = sys.argv[1]
new_pics = sys.argv[2]

if not os.path.exists(new_pics):
	os.makedirs(new_pics)

for imagename in os.listdir(current_pics):
	img = Image.open(f'{current_pics}{imagename}')
	split_name = os.path.splitext(imagename)[0]
	img.save(f'{new_pics}{split_name}.png', 'png')
print ('all done!')


