import cv2
import imutils

def rotateImage(fileName, outputFileName): 
    image = cv2.imread(fileName)
    
    new_image = imutils.rotate(image, angle=270)
    new_image = cv2.flip(new_image, 0)
    new_image = cv2.rotate(new_image, cv2.ROTATE_180)

    cv2.imwrite(outputFileName, new_image)
