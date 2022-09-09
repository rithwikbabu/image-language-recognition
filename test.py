from PIL import Image
from os import walk

# Prints Filesnames
filenames = next(walk("en_sample"), (None, None, []))[2]  # [] if no file
print(filenames)

# #read the image
# img = Image.open("en_sample/0.jpg")

# #show images
# img.show

 