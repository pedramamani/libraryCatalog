import json
import jinja2
from config import *

filterGenre = 'fiction'

def main():
    with open(booksFile, 'r') as file:
        data = json.load(file)
    books = sorted(filter(lambda b: b['genre'] == filterGenre, data.values()), key=lambda b: b['lastName'])

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(htmlPath))
    template = env.get_template('template.html')
    html = template.render(books=books)
    
    with open(htmlPath / f'{filterGenre}.html', 'w+') as file:
        file.write(html)

if __name__ == '__main__':
    main()