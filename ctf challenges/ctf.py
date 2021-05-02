from PIL import Image
from numpy import array,zeros,uint8

img1 = Image.open('scrambled1.png')
img2 = Image.open('scrambled2.png')
width = img1.width
height = img1.height

img_array=zeros([width,height,3],dtype=uint8)
arr1 = array(img1)
arr2 = array(img2)

for i in range(width):
    for j in range(height):
        img_array[i][j] = arr1[i][j]+arr2[i][j]

img = Image.fromarray(img_array)
img.show()
