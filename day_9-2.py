file1 = open('day_9-in.txt', 'r')
numbers = file1.readlines()
missing_number = 1721308972

possible_sums = set()
for index, start_number in enumerate(numbers):
    sum = 0
    numbers_in_sum = []
    while sum < missing_number:
        numbers_in_sum.append(int(numbers[index]))
        sum += int(numbers[index])
        if sum == missing_number:
            print(numbers_in_sum)
            print(min(numbers_in_sum), max(numbers_in_sum))
            print(min(numbers_in_sum) + max(numbers_in_sum))
        index += 1
        
            
        
    


