import sys

file1 = open('day_13-in.txt', 'r')
lines = file1.readlines()
array = lines[1].split(',')
bus_array = []
max = (-1, 0)
for index, item in enumerate(array):
    if item != 'x':
        item = int(item)
        bus_array.append((index, item))
        
def find_minute_apart(item, starting_point, increment_amount):
    number = starting_point
    while True:
        if (number + item[0]) % item[1] == 0:
            return number
        number += increment_amount

increment_amount = 1
starting_point = 0
for index, bus in enumerate(bus_array):
    if index > 0:
        starting_point = find_minute_apart(bus, starting_point, increment_amount)
    increment_amount *= bus[1]
print(starting_point)
    