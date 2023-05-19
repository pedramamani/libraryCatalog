import xlrd
import pathlib
import json
from config import *


libraryFilePath = assetsPath / 'MyLibraryByAuthor.xls'
headers = {'authors': 0, 'title': 1, 'coverPath': 12}
urlData = None

def createAuthor(authorString):
    lastName, firstName = authorString.split(', ')
    return dict(firstName=firstName, lastName=lastName)


def createBook(values, urlData):
    authorList = [createAuthor(a) for a in values[headers['authors']].split('; ')]
    title = values[headers['title']]
    id = pathlib.Path(values[headers['coverPath']]).stem
    coverUrl = urlData.get(id)
    return dict(id=id, authorList=authorList, title=title, coverUrl=coverUrl, genre='fiction')


def main():
    with open(urlsFilePath, 'r') as urlsFile:
        urlData = json.load(urlsFile)
    workbook = xlrd.open_workbook(libraryFilePath)
    mainSheet = workbook.sheet_by_index(0)
    
    with open(booksFilePath, 'r') as file:
        data = json.load(file)
        
    for rowIndex in range(1, mainSheet.nrows):
        book = createBook(mainSheet.row_values(rowIndex), urlData)
        if book['id'] not in data:
            data[book['id']] = book
    
    with open(booksFilePath, 'w+') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()
