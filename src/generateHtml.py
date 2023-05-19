import json
import jinja2
from config import *

filterGenre = 'fiction'

def main():
    with open(booksFilePath, 'r') as file:
        data = json.load(file)
    books = {k: b for k, b in data.items() if b.get('genre') == filterGenre}

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(htmlPath))
    template = env.get_template(templateFileName)
    html = template.render(books=books)
    
    with open(htmlPath / f'{filterGenre}.html', 'w+') as file:
        file.write(html)

if __name__ == '__main__':
    main()