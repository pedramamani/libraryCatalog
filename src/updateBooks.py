import xlrd
import pathlib
import json
from config import *


libraryFile = assetsPath / 'MyLibraryByAuthor.xls'
coverUrlTemplate = 'https://raw.githubusercontent.com/pedramamani/libraryCatalog/main/assets/images/{}.png'
headers = {'authors': 0, 'title': 1, 'coverPath': 12}


def createBook(values):
    id = pathlib.Path(values[headers['coverPath']]).stem
    title = values[headers['title']]
    firstAuthor = values[headers['authors']].split('; ')[0]
    lastName, firstName = firstAuthor.split(', ')
    coverUrl = coverUrlTemplate.format(id)
    return dict(id=id, title=title, firstName=firstName, lastName=lastName, coverUrl=coverUrl, genre='fiction')


def main():
    workbook = xlrd.open_workbook(libraryFile)
    mainSheet = workbook.sheet_by_index(0)
    
    with open(booksFile, 'r') as file:
        data = json.load(file)
        
    for rowIndex in range(1, mainSheet.nrows):
        book = createBook(mainSheet.row_values(rowIndex))
        if book['id'] not in data:
            data[book['id']] = book
    
    with open(booksFile, 'w+') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    main()
