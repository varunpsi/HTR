import numpy as np
from gtts import gTTS
import os
import cv2
from skimage.filters import threshold_local
import math
import pytesseract
from scipy import ndimage


def scan_view(img):
                
    # Defining the image name
    #img = "image1.jpg"

    image = cv2.imread(img)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thr = threshold_local(image,11,offset = 10,method="gaussian")
    image = (image > thr).astype("uint8") * 255

                # Scanning the image -> B&W scheme
                #scanned_im = Scan_View(img, save_collage=False, resize_collage=False, resize_height =500)
                #resized = Resize_Image(512, scanned_im)
                #scanned_im = "Scanned_Image.png"
                #img_new = cv2.imread(image)
                
    #cv2.imshow("Resized", image)
    #cv2.waitKey(0)
    return image



