file1 = open('day_1_in.txt', 'r')
Lines = file1.readlines()
set = set()

for line in Lines:
    item = int(line.strip())
    if item in set:
        print(item * (2020 - item))
    set.add(2020 - item)
    
