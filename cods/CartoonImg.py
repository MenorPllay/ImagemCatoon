import cv2 
import numpy as np 

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
# image_dir = str(os.path.join(BASE_DIR, 'media'))
image_dir = str(os.path.join(BASE_DIR))

img = ''


def cartoonimg(img):

    img_back = img
    img_dir = image_dir+'\\'
    img = img_dir+img

    img = cv2.imread(img) 

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 1) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  
                                            cv2.THRESH_BINARY, 5, 5) 
    
    color = cv2.bilateralFilter(img, 9, 250, 250) 
    cartoon = cv2.bitwise_and(color, color, mask=edges) 

    cv2.imwrite(img_dir+img_back+"-edges.jpeg", edges)
    cv2.imwrite(img_dir+img_back+"-Cartoon.jpeg", cartoon)

    back = [img_back+"-edges.jpeg",img_back+"-Cartoon.jpeg"]

    # back = img

    return back