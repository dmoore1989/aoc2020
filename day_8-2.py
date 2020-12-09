file1 = open('day_8-in.txt', 'r')
code = file1.readlines()
acc_sum = 0
curr_line = 0

def check_code(code, curr_line, acc):
    visited_procedures = set()
    while curr_line < len(code):
        code_line = code[curr_line]
        if curr_line in visited_procedures:
            return False
        visited_procedures.add(curr_line)
        if code_line[0:3] == 'acc':
            acc += int(code_line[4:])
            curr_line += 1
        elif code_line[0:3] == 'jmp':
            curr_line += int(code_line[4:])
        else:
            curr_line += 1

    return acc
    
        

while True:
    code_line = code[curr_line]
    if code_line[0:3] == 'acc':
        acc_sum += int(code_line[4:])
        curr_line += 1
    elif code_line[0:3] == 'jmp':
        if check_code(code, curr_line + 1, acc_sum):
            print(check_code(code, curr_line + 1, acc_sum))
            break
        curr_line += int(code_line[4:])
    else:
        if check_code(code, curr_line + int(code_line[4:]), acc_sum):
            print(check_code(code, curr_line + int(code_line[4:]), acc_sum))
            break
        curr_line += 1