import sys

file1 = open('day_13-in.txt', 'r')
lines = file1.readlines()
time = int(lines[0])
bus_array = lines[1].split(',')
earliest_wait = sys.maxsize
earliest_bus = 0
for bus in bus_array:
    if bus == 'x':
        continue
    bus = int(bus)
    next_bus = (bus * (time//bus + 1)) - time
    if next_bus < earliest_wait:
        earliest_wait = next_bus
        earliest_bus = bus
print(earliest_wait * earliest_bus)