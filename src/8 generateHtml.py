import json
import jinja2
from config import *
import os


def authorLastName(book):
    return book.get('author').split(' ')[-1]

def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(htmlPath))
    template = env.get_template('template.html')
    
    with open(dbPath / 'book.json', 'r') as file:
        data = json.load(file)
    
    for genre in os.listdir(scanPath):
        books = filter(lambda b: b['genre'] == genre, data.values())
        books = sorted(books, key=authorLastName)
        html = template.render(books=books)
        
        with open(htmlPath / f'{genre}.html', 'w+', encoding='utf-8') as file:
            file.write(html)

if __name__ == '__main__':
    main()