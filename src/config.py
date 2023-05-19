import pathlib

basePath = pathlib.Path(__file__).parent.parent.absolute()
assetsPath = basePath / 'assets'
imagesPath = assetsPath / 'images'
htmlPath = assetsPath / 'html'
jsonPath = assetsPath / 'json'

credsFilePath = jsonPath / 'creds.json'
tokenFilePath = jsonPath / 'token.json'
urlsFilePath = jsonPath / 'urls.json'
booksFilePath = jsonPath / 'books.json'

templateFileName = 'template.html'

scopes = ['https://www.googleapis.com/auth/drive']