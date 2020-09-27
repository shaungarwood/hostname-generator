#!/usr/bin/env python

import random
from sys import exit

with open("adjectives.txt", 'r') as f:
    adj = f.read().splitlines()

with open("nouns.txt", 'r') as f:
    nouns = f.read().splitlines()

try:
    while True:
        print(random.choice(adj) + "-" + random.choice(nouns))
        input()
except KeyboardInterrupt:
    exit(0)
