file1 = open('day_1_in.txt', 'r')
Lines = file1.readlines()
possible_sums = []

for line in Lines:
    item = int(line.strip())
    possible_sums.append(2020 - item)
    
for possible_sum in possible_sums:
    set = set()
    for line in Lines:
        item = int(line.strip())
        if item in set:
            print(item, 2020 - possible_sum, possible_sum - item)
            print(item * (2020 - possible_sum) * (possible_sum - item))
        set.add(possible_sum - item)
    del set

