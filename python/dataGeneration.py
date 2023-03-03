from actions import read_from_Json
from random import Random
random = Random()
def dataGen():
    history = []
    data = read_from_Json("paddy")
    locations = data['account']['locations']
    for loc in locations:
        loc['count'] = loc['count']+ random.randrange(1,4)
    print(data)
# print(data['account']['locations'])

