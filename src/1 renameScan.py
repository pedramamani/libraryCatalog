from config import *
import os
import string
import re
import random

idPattern = re.compile(r'^[a-zA-Z0-9]{8}$')


def randomId():
    chars = random.choices(string.ascii_letters + string.digits, k=8)
    return ''.join(chars)


def main():
    genres = os.listdir(scanPath)

    for genre in genres:
        genrePath = scanPath / genre
        for fileName in os.listdir(genrePath):
            stem = fileName.split('.')[0]
            if not re.match(idPattern, stem):
                newName = f'{randomId()}.jpg'
                os.rename(genrePath / fileName, genrePath / newName)


if __name__ == '__main__':
    main()
