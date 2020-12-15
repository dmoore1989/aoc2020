file1 = open('day_15-in.txt', 'r')
initial_numbers = file1.read().strip().split(',')
# mapping= {number: index for index, number in enumerate(numbers)}
mapping = {}
numbers = []
number_index = 0
while number_index < 2020:
    if number_index < len(initial_numbers):
        number = int(initial_numbers[number_index])
    elif numbers[number_index - 1] in mapping:
        # print(number_index, mapping, mapping[numbers[number_index - 1]]) 
        number = (number_index - 1) - mapping[numbers[number_index - 1]]
    else:
        number = 0
    numbers.append(number)
    mapping[numbers[number_index - 1]] = number_index - 1
    # print(mapping)
    number_index += 1
    # print(numbers)
print(numbers[2019])
