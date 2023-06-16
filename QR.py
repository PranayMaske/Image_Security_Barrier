import cv2
import numpy as np
import easyocr
import pyzbar
import matplotlib.pyplot as plt

from pyzbar.pyzbar import decode

img = cv2.imread('C:/Users/Pranay/Desktop/ISB Sample imges/Sample1.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
code = decode(img)
print(code)


for barcode in decode(img):
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    #cv2.polylines(img,[pts],True,color=(0, 255, 0), thickness=10)
    cv2.drawContours(img,[pts],-1,color=(255,0,0),thickness=-1)
    plt.imshow(img)
    plt.show()

'''for barcode in decode(img):
    pts = np.array([barcode.polygon],np.int32)
    pts = pts.reshape((-1,1,2))
    cv2.polylines(img,[pts],True,(255,0,255),10)
    plt.imshow(img)
    plt.show()'''