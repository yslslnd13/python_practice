import sys

target = sys.argv[1]
data = ''

with open(target, 'r') as f:
    data = f.read()

data = data.replace('\t', '    ')

with open(target, 'w') as f:
    f.write(data)