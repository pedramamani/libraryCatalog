from config import *
import requests
import json
import cv2


def search(query):
    response = requests.get(url='https://www.googleapis.com/books/v1/volumes', params={
        'key': env['booksApiKey'],
        'q': query,
        'printType': 'books',
        'projection': 'lite',
        'orderBy': 'relevance',
        'startIndex': '0',
        'maxResults': '12'
    })
    data = response.json()

    results = []
    if not data.get('items'):
        return results
    for item in data.get('items'):
        info = item.get('volumeInfo')
        title, authors = info.get('title'), info.get('authors')
        if title and authors:
            results.append({'title': title, 'author': authors[0]})
    return results[:10]


def main():
    with open(dbPath / 'query.json', 'r') as file:
        queryById = json.load(file)
    with open(dbPath / 'title.json', 'r') as file:
        titleById = json.load(file)
    
    for id, query in queryById.items():
        if id in titleById:
            continue
        
        image = cv2.imread(str(coverPath / f'{id}.jpg'))
        cv2.imshow('Image', image)

        found = False
        while not found:
            print(f'Searching for "{query}":')
            results = search(query)
            for index, result in enumerate(results):
                print(f'{index}. {result.get("title")} - {result.get("author")}')
            
            key = cv2.waitKey()
            selection = key - 48
            if 0 <= selection < len(results):
                titleById[id] = results[selection]
                found = True
            elif key == ord('s'):
                print()
                query = input('Enter search query: ')
                continue
            elif key == ord('q'):
                return
        print('-' * 50)

        with open(dbPath / 'title.json', 'w+') as file:
            json.dump(titleById, file, indent=4)


if __name__ == '__main__':
    main()