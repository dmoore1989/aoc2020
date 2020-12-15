import sys
import re

bitmask_pattern = r'mask = ([0|1|X]+)'
mapping_pattern = r'mem\[([0-9]+)\] = ([0-9]+)'
file1 = open('day_14-in.txt', 'r')
lines = file1.readlines()
mapping = {}
for line in lines:
    line = line.strip()
    if line[0:4] == 'mask':
        bitmask = re.match(bitmask_pattern, line)[1]
    else:
        parsed_assignment= re.match(mapping_pattern, line)
        key = int(parsed_assignment[1])
        number = bin(int(parsed_assignment[2]))[2:]
        expanded_bin = list('0' * (36 - len(number)) + number)
        for pos, bit in enumerate(bitmask):
            if (bit != 'X'):
                expanded_bin[pos] = bit
        mapping[key] = int(''.join(expanded_bin), 2)

print(sum(mapping.values())) 
