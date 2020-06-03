import os
import random
import json

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
motto_lib = os.path.join(PROJECT_ROOT, 'motto.json')

with open(motto_lib, 'r', encoding='utf8') as read_motto:
    jMotto = json.load(read_motto)


random_reply = random.choice(jMotto['MOTTO'])

print(random_reply)
