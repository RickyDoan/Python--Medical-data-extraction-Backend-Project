from pdf2image import convert_from_path
import pytesseract
import numpy as np
import cv2 as cv

PATH_POPPLER = '/usr/local/Cellar/poppler/24.04.0_1/bin'

def get_text_from_pdf(image):
    holder = ''
    page_pdf = convert_from_path(image, poppler_path=PATH_POPPLER)
    for page_num, page in enumerate(page_pdf):
        page1 = np.array(page)
        page_grayScale = cv.cvtColor(page1, cv.COLOR_BGR2GRAY)
        page_resized = cv.resize(page_grayScale, None, fx=0.8, fy=0.8, interpolation=cv.INTER_LINEAR)
        th = cv.adaptiveThreshold(page_resized, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                  cv.THRESH_BINARY, 65, 14)
        text_from_pdf = pytesseract.image_to_string(th, lang='eng')
        holder += f"page {page_num + 1}:\n {text_from_pdf}\n"
        return holder