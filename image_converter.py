from PIL import Image

import imgrotate

imageName = "img.jpg"#input("Input filename: ")
outputFileName = "img.myimg"#input("Output filename: ")

def format_number(num):
    return "${0:03}".format(num)[1:]

imgrotate.rotateImage(imageName, "rotated_img.png")
im = Image.open("rotated_img.png")

pixels = list(im.getdata())
imageString = "["
index = -1
width, height = im.size

for _ in pixels:
    index += 1

    imageString += "@" + format_number(pixels[index][0]) + format_number(pixels[index][1]) + format_number(pixels[index][2]) + ""
    
imageString += "]!" + str(width) + "!" + str(height)

with open(outputFileName, "w") as f:
    f.write(imageString)

exec(open("main.py").read())