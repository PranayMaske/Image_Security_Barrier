
import cv2
import numpy as np
import easyocr  #For OCR
import matplotlib.pyplot as plt
import re
#%matplotlib inline

from pyzbar.pyzbar import decode

#im_1_path = 'C:/Users/HP/Desktop/ISB Sample imges/Untitled design (8).png'
im_1_path = 'C:/Users/HP/Desktop/ISB Sample imges/Aadhaar.png'
#im_1_path = 'C:/Users/HP/Desktop/ISB Sample imges/Picture1.png'

def recognize_text(img_path):
    reader = easyocr.Reader(['en'])
    return reader.readtext(img_path)

def overlay_ocr_text(img_path, save_name):
    # loads image
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    fig_width = 10  # initialize to a default value
    dpi = 10
    fig_height = int(img.shape[1] / dpi)
    if img.shape[0] > img.shape[1]:
        # adjust fig_width based on image aspect ratio
        fig_width = int(img.shape[1] / img.shape[0] * fig_height)
    plt.figure()
    f, axarr = plt.subplots(1, 2, figsize=(fig_width, fig_height))
    axarr[0].imshow(img)

    # recognize text
    result = recognize_text(img_path)


# QR and bar code detection START

    code = decode(img)
    print(code)

    for barcode in decode(img):
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))

        cv2.drawContours(img, [pts], -1, color=(255, 0, 0), thickness=-1)

    for (bbox, text, prob) in result:
        if prob >= 0.5:
            # display
            print(f' {text} ')
            print(len(text))

            (top_left, top_right, bottom_right, bottom_left) = bbox
            top_left = (int(top_left[0]), int(top_left[1]))
            bottom_right = (int(bottom_right[0]), int(bottom_right[1]))
            print(top_left)
            print(bottom_right)


            string1 = text

            # opening a text file
            file1 = open("sensitive_words.txt", "r")

            # read file content
            readfile = file1.read()


            if string1 in readfile:
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)
            else:
                print('String', string1, 'Not Found')

            # closing aA file
            file1.close()


            # old version
            # apn image ke har sensitiv words ke liye if else condition nhi dal skte,
            # if (text == 'Certificate ID' or text == 'certificate ID' or text == 'ID' or text == 'ID' or text == 'ID'):
            # cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=15)

            # if (text == 'Certificate ID') :
            # cv2.rectangle(img=img, pt1=(35, 191), pt2=(300, 210), color=(0, 255, 0), thickness=15)

            # if (text == 'Name:') :
            # cv2.rectangle(img=img, pt1=top_left, pt2=(642, 292), color=(0, 255, 0), thickness=15)

            '''if (text == 'FQMRT8262D') :
              cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)'''

            # if (text == 'Password:') :
            # cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=15)

             #cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=15)
             #put recognized text
             #cv2.putText(img=img, text=text, org=(top_left[0], top_left[1] - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=2, color=(0, 255, 0), thickness=5)
            num = text.strip()
            nuk = (len(num))
            if nuk == 10 and all(map(str.isalpha, num[:5])) and all(map(str.isnumeric, num[5:9])) and num[9].isalpha():
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)
            else:
                print("This is not a PAN card.")
            if nuk == 8 and re.match(r'^[A-Z]{3}\d{3}[A-Z]\d$', num):
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)

            if nuk == 14 and re.match(r'^\d{4} \d{4} \d{4}$', num):
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)
            else:
                print("This is not a adhh card.")

            if "+91" in num:
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)

            if "Plot no" in num:
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)

            if "1234" in num:
                cv2.rectangle(img=img, pt1=top_left, pt2=bottom_right, color=(0, 255, 0), thickness=-1)

# show and save image
    axarr[1].imshow(img)
    plt.savefig(f'Output/{save_name}_overlay.png', bbox_inches='tight')



overlay_ocr_text(im_1_path,'Pranay')


