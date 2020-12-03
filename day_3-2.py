file1 = open('day_3_in.txt', 'r')
Lines = file1.readlines()

path = []
for line in Lines:
    path.append(line.strip())

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
tree_count_mult = 1
for slope in slopes:
    x = 0
    y =0
    x_change = slope[0]
    y_change = slope[1]
    tree_count = 0
    while y < len(path):
        if path[y][x % len(path[y])] == '#':
            tree_count += 1
        x += x_change
        y += y_change
    print(tree_count)

    tree_count_mult = tree_count_mult * tree_count
print(tree_count_mult)