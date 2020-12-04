import re

def validate_datum(code, value):
    if code == 'byr':
        return int(value) >= 1920 and int(value) <= 2002
    elif code == 'iyr':
        return int(value) >= 2010 and int(value) <= 2020
    elif code == 'eyr':
        return int(value) >= 2020 and int(value) <= 2030
    elif code == 'hgt':
        unit = value[-2:]
        size = value[0:-2]
        if unit == 'in':
            return int(size) >= 59 and int(size) <= 76
        elif unit == 'cm':
            return int(size) >= 150 and int(size) <= 193
        else:
            return False
    elif code == 'hcl':
        return bool(re.match(r'#([0-9|a-z]){6}$', value))
    elif code == 'ecl':
        return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    elif code == 'pid':
        return bool(re.match(r'^[0-9]{9}$', value))

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
    datum_count = 0
    data = re.findall(r'(\w*:(\w|#)*)', passport)
    for datum in data:
        code, value = datum[0].split(':')
        print(code,value, validate_datum(code, value))
        if code in valid_fields and validate_datum(code, value):
            datum_count += 1
    if datum_count == 7:
        print('yes')
        valid_passports += 1
    print('---')

print(valid_passports)

