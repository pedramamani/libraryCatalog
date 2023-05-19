from config import *
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json

driveFolderId = '13tVoDT8YRwGbhEPYlOZ7zrrbKpbjW6mI'
fileUrlTemplate = 'https://drive.google.com/uc?export=view&id={0}'

def main():
    service = build('drive', 'v3', credentials=Credentials.from_authorized_user_file(tokenFilePath, scopes))
    response = service.files().list(q=f"'{driveFolderId}' in parents", fields='files(id, name)').execute()
    data = {}
    
    for metadata in response.get('files'):
        id, name = metadata.get('id'), metadata.get('name')
        stem = name.split('.')[0]
        url = fileUrlTemplate.format(id)
        data[stem] = url
    
    with open(urlsFilePath, 'w+') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':
    main()
