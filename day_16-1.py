import re

file1 = open('day_16-in.txt', 'r')
lines = file1.readlines()
index = 0
line = lines[index].strip()
typere = r'[a-z ]+: ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'
lineset = set()
missing_values = []
while line != '':
    match = re.match(typere, line)
    print(match)
    lineset |= set(range(int(match[1]), int(match[2]) + 1))
    lineset |= set(range(int(match[3]), int(match[4]) + 1 ))
    index += 1
    line = lines[index].strip()
print(lineset)
index += 5
while index < len(lines):
    values = lines[index].strip().split(',')
    for value in values:
        if int(value) not in lineset:
            print(value)
            missing_values.append(int(value))
    index += 1
print(sum(missing_values))

