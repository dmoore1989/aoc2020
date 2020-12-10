file1 = open('day_8-in.txt', 'r')
code = file1.readlines()
visited_procedures = set()
acc_sum = 0
curr_line = 0

while True:
    if curr_line in visited_procedures:
        print(acc_sum)
        break
    visited_procedures.add(curr_line)
    code_line = code[curr_line]
    if code_line[0:3] == 'acc':
        acc_sum += int(code_line[4:])
        curr_line += 1
    elif code_line[0:3] == 'jmp':
        curr_line += int(code_line[4:])
    else:
        curr_line += 1
        
        