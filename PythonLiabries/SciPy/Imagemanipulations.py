import imageio
from imageio import imread, imsave
import
img = imread('C:\\Users\\sunil\\OneDrive\\Desktop\\Sunil Images\\sunilIImg1.jpg')
print(img.shape)
print(img.dtype)
# Tinting The Image
img_tint = img*[1,0.45,0.3]
imsave('C:\\Users\\sunil\\OneDrive\\Desktop\\Sunil Images\\sunilIImg21.jpg')
# resising the Tinted imgage to be 300 x 300 pixels

img_tint_resize = imr