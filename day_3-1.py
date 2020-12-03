file1 = open('day_3_in.txt', 'r')
Lines = file1.readlines()

path = []
for line in Lines:
    path.append(line.strip())

x = 0
tree_count = 0
for row in path:
    if row[x % len(row)] == '#':
        tree_count += 1
    x += 3

print(tree_count)
    