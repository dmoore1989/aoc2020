import sys
import re

bitmask_pattern = r'mask = ([0|1|X]+)'
mapping_pattern = r'mem\[([0-9]+)\] = ([0-9]+)'
file1 = open('day_14-in.txt', 'r')
lines = file1.readlines()
mapping = {}
def parse_binary_num(binary_num):
    if(len(binary_num) == 1):
        return [binary_num[0]] if binary_num[0] != 'X' else ['0', '1'] 
    elif binary_num[0] == 'X':
        return parse_binary_num('0' + binary_num[1:]) + parse_binary_num('1' + binary_num[1:])
    num_array = parse_binary_num(binary_num[1:])
    return [binary_num[0] + num for num in num_array]

for line in lines:
    line = line.strip()
    if line[0:4] == 'mask':
        bitmask = re.match(bitmask_pattern, line)[1]
    else:
        parsed_assignment= re.match(mapping_pattern, line)
        key = bin(int(parsed_assignment[1]))[2:]
        number = int(parsed_assignment[2])
        expanded_bin = list('0' * (36 - len(key)) + key)
        for pos, bit in enumerate(bitmask):
            if bit in ('X', '1'):
                expanded_bin[pos] = bit
        keys = parse_binary_num(''.join(expanded_bin))
        for key in keys:
            mapping[key] = number

print(sum(mapping.values())) 