import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from config import *

def main():
    creds = None
    if os.path.exists(tokenFilePath):
        creds = Credentials.from_authorized_user_file(tokenFilePath, scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credsFilePath, scopes)
            creds = flow.run_local_server(port=0)
        with open(tokenFilePath, 'w') as token:
            token.write(creds.to_json())


if __name__ == '__main__':
    main()
