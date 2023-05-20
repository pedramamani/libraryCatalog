import cv2 
import pytesseract
from config import *
import os
import re
import requests


def main():
    for fileName in os.listdir(croppedPath):
        img = cv2.imread(str(croppedPath / fileName), cv2.IMREAD_GRAYSCALE)
        cv2.imshow('Image', img)
        if cv2.waitKey() == ord('q'):
            cv2.destroyAllWindows()
            return

        custom_config = r'--psm 4 -c tessedit_char_whitelist=" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"' # 4, 11
        result = pytesseract.image_to_string(img, lang='eng', config=custom_config)
        result = re.sub('\s+', ' ', result).strip()

        if not result:
            continue

        response = requests.get(url='https://www.googleapis.com/books/v1/volumes', params={
            'q': result,
            'printType': 'books',
            'projection': 'lite',
            'orderBy': 'relevance',
            'startIndex': '0',
            'maxResults': '10',
            'key': ''
        })
        data = response.json()

        if not data.get('items'):
            continue

        for index, item in enumerate(data.get('items')):
            info = item.get('volumeInfo')
            print(f'{index + 1}.', info.get('title'), info.get('authors'))


if __name__ == '__main__':
    main()