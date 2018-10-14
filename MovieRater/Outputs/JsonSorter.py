import json

with open('numTitles.json') as f:
    data = json.load(f)

    data.sort(key=operator.itemgetter('imdbRating'))

    json.dump(data)
