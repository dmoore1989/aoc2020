file1 = open('day_9-in.txt', 'r')
numbers = file1.readlines()

def valid_number(number, check_arr):
    possible_sums = set()
    for check_num in check_arr:
        if number/2 == check_num:
            continue
        possible_sums.add(number - check_num)
    for check_num in check_arr:
        if check_num in possible_sums:
            return True
    return False          



check_arr = []
for number in numbers:
    number = int(number)
    if len(check_arr) > 25:
        check_arr = check_arr[1:]
        if not valid_number(number, check_arr):
            print(number)
            break
    check_arr.append(number)