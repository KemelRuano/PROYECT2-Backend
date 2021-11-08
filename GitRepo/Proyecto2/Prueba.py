import json

with open('c:\Phyton\GitRepo\Proyecto2\ok.json') as f:
 data = json.load(f)

for state in data['images']:
    print(state)
for s in data['videos']:
    print(s)
