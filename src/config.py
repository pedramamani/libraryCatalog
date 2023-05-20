import pathlib

basePath = pathlib.Path(__file__).parent.parent.absolute()
assetsPath = basePath / 'assets'
imagesPath = assetsPath / 'images'
htmlPath = assetsPath / 'html'
scansPath = assetsPath / 'scans'
croppedPath = assetsPath / 'cropped'
booksFile = assetsPath / 'books.json'
