import re

file1 = open('day_2_in.txt', 'r')
Lines = file1.readlines()

correct_passwords = 0 
print(len(Lines))
for line in Lines:
    line_breakdown = re.match(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
    min = int(line_breakdown[1])
    max = int(line_breakdown[2])
    letter = line_breakdown[3]
    password = line_breakdown[4]
    count = 0
    for test_letter in password:
        if test_letter == letter:
            count += 1
    if count >= min and count <= max:
        correct_passwords += 1
        
print(correct_passwords)