import cv2
import numpy as np

# load a color image as grayscale, convert it to false color, and save false color version    
im_gray = cv2.imread('noalign_color.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imwrite('gray_image_original.png', im_gray)
im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)
cv2.imwrite('colormap.png', im_color) # save in lossless format to avoid colors changing

# create an inverse from the colormap to gray values
gray_values = np.arange(256, dtype=np.uint8)
color_values = map(tuple, cv2.applyColorMap(gray_values, cv2.COLORMAP_JET).reshape(256, 3))
color_to_gray_map = dict(zip(color_values, gray_values))

# load false color and reserve space for grayscale image
false_color_image = cv2.imread('colormap.png')

# apply the inverse map to the false color image to reconstruct the grayscale image
gray_image = np.apply_along_axis(lambda bgr: color_to_gray_map[tuple(bgr)], 2, false_color_image)

# save reconstructed grayscale image
cv2.imwrite('gray_image_reconstructed.png', gray_image)

# compare reconstructed and original gray images for differences
print('Number of pixels different:', np.sum(np.abs(im_gray - gray_image) > 0))

