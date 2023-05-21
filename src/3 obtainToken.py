from config import *
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow


def main():
    credentials = None
    tokenFile = secretPath / 'token.json'
    if os.path.exists(tokenFile):
        credentials = Credentials.from_authorized_user_file(tokenFile, scopes)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(secretPath / 'client.json', scopes)
            credentials = flow.run_local_server(port=0)
        with open(tokenFile, 'w+') as token:
            token.write(credentials.to_json())


if __name__ == '__main__':
    main()
