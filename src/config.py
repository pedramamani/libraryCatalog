import pathlib
import dotenv 

rootPath = pathlib.Path(__file__).parent.parent.absolute()
env = dotenv.dotenv_values(rootPath / '.env')
scopes = ['https://www.googleapis.com/auth/cloud-vision']

coverPath = rootPath / 'asset/image/cover'
scanPath = rootPath / 'asset/image/scan'
secretPath = rootPath / 'secret'
dbPath = rootPath / 'asset/db'
htmlPath = rootPath / 'asset/html'