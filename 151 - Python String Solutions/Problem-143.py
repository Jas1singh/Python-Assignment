# Problem 143:

import json

s = '{"key": "value"}'

try:
    json.loads(s)
    print(True)
except:
    print(False)
