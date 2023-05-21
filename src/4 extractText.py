from config import *
import os
from google.cloud import vision
from google.oauth2.credentials import Credentials
import json
import math


def rectangleDimensions(vertices):
    n = len(vertices)
    distances = []
    for i in range(n):
        a, b = vertices[i], vertices[(i + 1) % n]
        distance = math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)
        distances.append(distance)
    
    height = int(round(min(distances)))
    width = int(round(max(distances)))
    return height, width


def main():
    creds = Credentials.from_authorized_user_file(secretPath / 'token.json', scopes)
    client = vision.ImageAnnotatorClient(credentials=creds)

    with open(dbPath / 'text.json', 'r') as file:
        textById = json.load(file)
    
    for fileName in os.listdir(coverPath):
        id = fileName.split('.')[0]
        if id in textById:
            continue

        with open(coverPath / fileName, 'rb') as file:
            content = file.read()
        image = vision.Image(content=content)
        response = client.text_detection(image=image)
        annotations = response.text_annotations

        words = []
        for annotation in annotations[1:]:
            height, width = rectangleDimensions(annotation.bounding_poly.vertices)
            words.append({'height': height, 'width': width, 'word': annotation.description})
        text = annotations[0].description if len(annotations) > 0 else ''
        textById[id] = {'description': text, 'words': words}
    
        with open(dbPath / 'text.json', 'w') as file:
            json.dump(textById, file, indent=4)


if __name__ == '__main__':
    main()