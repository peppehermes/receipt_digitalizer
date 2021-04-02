from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pytesseract
from pytesseract import Output
import re


# Read the image
img = cv2.imread("ita.jpg", 0)


# Simple thresholding
# ret, thresh1 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
thresh1 = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
)
# cv2.imshow("gray", img)

d = pytesseract.image_to_data(img, output_type=Output.DICT)
extracted_text = pytesseract.image_to_string(img, lang="ita")
# print(extracted_text)

# cv2.imshow("img", thresh1)

# cv2.imshow("img", img)
# cv2.waitKey(0)

# receipt_ocr = {}

splits = extracted_text.splitlines()
print(splits[6])
# restaurant_name = splits[0] + "" + splits[1]

# # regex for date. The pattern in the receipt is in 30.07.2007 in DD:MM:YYYY

# date_pattern = r"(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d"
# date = re.search(date_pattern, extracted_text).group()
# receipt_ocr["date"] = date
# print(date)