import os

with open(os.path.dirname(__file__) + '/static/par.txt', 'r') as f:
    print(f.read())
