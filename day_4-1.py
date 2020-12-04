import re

file1 = open('day_4-in.txt', 'r')
text = file1.read()

passports = text.split('\n\n') 

valid_fields = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
]
valid_passports = 0
for passport in passports:
    code_count = 0
    codes = re.findall(r'(\w*)(?=:)', passport)
    for code in codes:
        if code in valid_fields:
            code_count += 1
    if code_count == 7:
        valid_passports += 1

print(valid_passports)