from config import *
import json
import re


def buildQuery(text):
    words = text.get('words')
    heights = [w.get('height') for w in words]
    thresholdHeight = max(heights) * 0.3
    words = [w for w in words if w.get('height') > thresholdHeight]

    query = ' '.join([w.get('word') for w in words])
    query = re.sub(r'[^a-zA-Z ]', ' ', query)
    query = re.sub(r'\s+', ' ', query).strip()
    return query


def main():
    with open(dbPath / 'text.json', 'r') as file:
        textById = json.load(file)
    with open(dbPath / 'supplement.json', 'r') as file:
        supplementById = json.load(file)

    queryById = {}
    for id, text in textById.items():
        if id in supplementById:
            queryById[id] = supplementById[id]
        else:
            queryById[id] = buildQuery(text)
    
    with open(dbPath / 'query.json', 'w+') as file:
        json.dump(queryById, file, indent=4)


if __name__ == '__main__':
    main()