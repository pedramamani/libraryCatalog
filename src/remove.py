from config import *
import os
import json

def main():
    with open(dbPath / 'text.json', 'r') as file:
        textById = json.load(file)
    with open(dbPath / 'query.json', 'r') as file:
        queryById = json.load(file)
    with open(dbPath / 'title.json', 'r') as file:
        titleById = json.load(file)
    with open(dbPath / 'supplement.json', 'r') as file:
        supplementById = json.load(file)
    with open(dbPath / 'book.json', 'r') as file:
        bookById = json.load(file)

    for fileName in os.listdir(rootPath / 'asset/image/misc/persian'):
        if fileName in os.listdir(coverPath):
            os.remove(coverPath / fileName)

        id = fileName.split('.')[0]
        if id in textById:
            textById.pop(id)
        if id in queryById:
            queryById.pop(id)
        if id in titleById:
            titleById.pop(id)
        if id in supplementById:
            supplementById.pop(id)
        if id in bookById:
            bookById.pop(id)
    
    with open(dbPath / 'text.json', 'w+') as file:
        json.dump(textById, file, indent=4)
    with open(dbPath / 'query.json', 'w+') as file:
        json.dump(queryById, file, indent=4)
    with open(dbPath / 'title.json', 'w+') as file:
        json.dump(titleById, file, indent=4)
    with open(dbPath / 'supplement.json', 'w+') as file:
        json.dump(supplementById, file, indent=4)
    with open(dbPath / 'book.json', 'w+') as file:
        json.dump(bookById, file, indent=4)


if __name__ == '__main__':
    main()
