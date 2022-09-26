from PIL import Image
from os import walk
import tempfile

# Prints Filesnames
filenames = next(walk("en_sample"), (None, None, []))[2]  # [] if no file
# print(filenames)

def set_image_dpi(image, dpiVal):
    """
    Rescaling image to 300dpi without resizing
    :param image: An image
    :return: A rescaled image
    """
    image_resize = image
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
    temp_filename = temp_file.name
    image_resize.save(temp_filename, dpi=(dpiVal, dpiVal))
    return temp_filename

# for name in filenames[0]:
    #read the image
name = filenames[0]
img = Image.open("en_sample/" + name)
# fetching the dimensions
print(img)
wid, hgt = img.size
print(str(wid) + " x " + str(hgt))
imgPath = set_image_dpi(img, 30)
img2 = Image.open(imgPath)
wid, hgt = img.size
print(str(wid) + " x " + str(hgt))
img.show()
img2.show()

#show images
# img.show

 