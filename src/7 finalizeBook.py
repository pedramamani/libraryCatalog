from config import *
import os
import json


coverUrlTemplate = 'https://raw.githubusercontent.com/pedramamani/libraryCatalog/main/asset/image/cover/{}.jpg'

def main():
    with open(dbPath / 'book.json', 'r') as file:
        bookById = json.load(file)
    with open(dbPath / 'title.json', 'r') as file:
        titleById = json.load(file)

    genres = os.listdir(scanPath)
    for genre in genres:
        genrePath = scanPath / genre
        for fileName in os.listdir(genrePath):
            id = fileName.split('.')[0]
            if id in bookById:
                continue
            book = titleById.get(id)
            book.update({'genre': genre, 'cover': coverUrlTemplate.format(id)})
            bookById[id] = book
    
        with open(dbPath / 'book.json', 'w+') as file:
            json.dump(bookById, file, indent=4)

if __name__ == '__main__':
    main()