import json
import os

import requests

plantname = "玉米"
with open(plantname + '.json', 'r') as f:
    piclist = json.load(f)
i = 1
os.system('mkdir ' + plantname)
for pic in piclist:
    r = requests.get(pic)
    with open(plantname + '/{}.jpg'.format(i), 'wb') as f:
        f.write(r.content)
    print(i)
    i += 1
