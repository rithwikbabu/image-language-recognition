import imageio as iio
 
# read an image
img = iio.imread("g4g.png")
 
# write it in a new format
iio.imwrite("g4g.jpg", img)