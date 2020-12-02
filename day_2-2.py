import re

file1 = open('day_2_in.txt', 'r')
Lines = file1.readlines()

correct_passwords = 0 
print(len(Lines))
for line in Lines:
    line_breakdown = re.match(r'([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', line)
    position_a = int(line_breakdown[1])
    position_b = int(line_breakdown[2])
    letter = line_breakdown[3]
    password = line_breakdown[4]
    if ((password[position_a - 1] == letter and password[position_b - 1] != letter) or
        (password[position_b - 1] == letter and password[position_a - 1] != letter)):
        correct_passwords += 1
        
print(correct_passwords)