import re

file1 = open('day_16-in.txt', 'r')
lines = file1.readlines()
index = 0
line = lines[index].strip()
typere = r'([a-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)'
cat_req = {}
lineset = set()
cat_map = {}
valids = []
while line != '':
    match = re.match(typere, line)
    category = match[1]
    lineset |= set(range(int(match[2]), int(match[3]) + 1))
    lineset |= set(range(int(match[4]), int(match[5]) + 1 ))
    cat_req[category] = set(range(int(match[2]), int(match[3]) + 1))
    cat_req[category] |= set(range(int(match[4]), int(match[5]) + 1 ))
    index += 1
    line = lines[index].strip()
index += 2
valids = [lines[index].strip().split(',')]
index += 3
while index < len(lines):
    valid_line = True
    values = lines[index].strip().split(',')
    for value in values:
        if int(value) not in lineset:
            valid_line = False
            break
    if valid_line:
        valids.append(values)
    index += 1
# print(valids)
index = 0
while index < len(cat_req):
    for cat, rule in cat_req.items():
        if cat not in cat_map:
            cat_map[cat] = set()
        valid_cat = True
        for valid in valids:
            if int(valid[index]) not in rule:
                # print(valid[index], rule)
                valid_cat = False
                break
        if valid_cat:
            cat_map[cat].add(index)
    index += 1

print(cat_map)
index = 0
final_rules = {}
while len(cat_map) > 0:
    approved_rules = []
    for cat, rules in cat_map.items():
        if index in rules:
            approved_rules.append(cat)
        if len(approved_rules) > 1:
            break    
    if len(approved_rules) == 1:
        final_rules[approved_rules[0]] = index
        del cat_map[approved_rules[0]]
    index = (index + 1) % len(valids[0])

print(final_rules)

valid_ticket_items = []
for cat, index in final_rules.items():
    if cat[0:9] == 'departure':
        valid_ticket_items.append(int(valids[0][index]))
print(valid_ticket_items)
print(valid_ticket_items[0] * valid_ticket_items[1] * valid_ticket_items[2] * valid_ticket_items[3] * valid_ticket_items[4] * valid_ticket_items[5])