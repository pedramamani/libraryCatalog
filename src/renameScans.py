from config import *
import os
import secrets
import string
import re

idPattern = re.compile(r'^[a-zA-Z0-9]{8}$')

def generateRandomId():
    chars = [secrets.choice(string.ascii_letters + string.digits) for _ in range(8)]
    return ''.join(chars)

def main():
    for fileName in os.listdir(scansPath):
        stem = fileName.split('.')[0]
        if re.match(idPattern, stem):
            continue
        id = generateRandomId()
        os.rename(scansPath / fileName, scansPath / f'{id}.jpg')


if __name__ == '__main__':
    main()
