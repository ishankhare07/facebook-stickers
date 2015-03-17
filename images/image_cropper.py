import PIL
from PIL import Image
import os
import sys

if not os.path.exists('../stickers/' + sys.argv[1]):
	os.makedirs('../stickers/' + sys.argv[1])

img = Image.open(sys.argv[1] + '.png')

x_parts = int(input('Enter number of columns'))
y_parts = int(input('Enter number of rows'))
width, height = img.size
left=0
top=0
right = int(width/x_parts)
bottom = int(height/y_parts)
current_bottom = bottom
for x in range(0,y_parts):
	left = 0
	current_right = right
	for y in range(0,x_parts):
		print(left,top,current_right,current_bottom)
		box = (left,top,current_right,current_bottom)
		new_img = img.crop(box)
		new_img.save('../stickers/' + sys.argv[1] + '/' + str(x) + ' ' + str(y) + '.png')
		new_img.load()
		left = current_right
		current_right += right
	top = current_bottom
	current_bottom += bottom
