import json
import operator
import sys

class JsonSorter:

    with open(sys.argv[1], 'r+') as f:
        data = json.load(f)

        data.sort(key=operator.itemgetter('name'))
        f.seek(0)
        json.dump(data, f, indent=0)
