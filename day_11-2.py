import copy
import json

file1 = open('day_11-in.txt', 'r')
lines = file1.readlines()
seating = []
for line in lines:
    seating.append(list(line.strip()))


seating_neighbors = (
    (0,1),
    (1,1),
    (1,0),
    (1, -1),
    (0, -1),
    (-1, -1),
    (-1, 0),
    (-1, 1),
)

def can_be_sat_in(x_index, y_index, seating):
    for seating_neighbor in seating_neighbors:
        incrementer = 1
        while True:
            if y_index + seating_neighbor[0] * incrementer >= len(seating) or y_index + seating_neighbor[0] * incrementer < 0: 
                break
            row = seating[y_index + seating_neighbor[0]* incrementer]
            if x_index + seating_neighbor[1] * incrementer >= len(row) or x_index + seating_neighbor[1] * incrementer < 0: 
                break
            if row[x_index + seating_neighbor[1] * incrementer ]== '#':
                return False
            if row[x_index + seating_neighbor[1] * incrementer] == 'L':
                break
            incrementer += 1
    return True

def should_be_emptied(x_index, y_index, seating):
    seats_full = 0
    for seating_neighbor in seating_neighbors:
        incrementer = 1
        while True:
            if y_index + seating_neighbor[0] * incrementer >= len(seating) or y_index + seating_neighbor[0] * incrementer < 0:
                break
            row = seating[y_index + seating_neighbor[0] * incrementer]
            if x_index + seating_neighbor[1] * incrementer >= len(row) or x_index + seating_neighbor[1] * incrementer < 0: 
                break
            if row[x_index + seating_neighbor[1] * incrementer] == '#':
                if y_index == 1 and x_index == len(seating) - 1:
                    print(seating_neighbor, incrementer)
                seats_full += 1
                break
            if row[x_index + seating_neighbor[1] * incrementer]  == 'L':
                break
            incrementer += 1
    if y_index == 1 and x_index == len(seating) - 1:
        print(seats_full)
    return seats_full >= 5

new_seating = copy.deepcopy(seating)
while True:
    seats_to_fill = []
    seats_to_empty = []
    for y_index, row in enumerate(seating):
        for x_index, seat in enumerate(row):
            if seat == 'L' and can_be_sat_in(x_index, y_index, seating):
                seats_to_fill.append((y_index, x_index))
            if seat == '#' and should_be_emptied(x_index, y_index, seating):
                seats_to_empty.append((y_index, x_index))

    for seat_to_fill in seats_to_fill:
        new_seating[seat_to_fill[0]][seat_to_fill[1]] = '#'

    for seat_to_empty in seats_to_empty:
        new_seating[seat_to_empty[0]][seat_to_empty[1]] = 'L'
    if json.dumps(new_seating) == json.dumps(seating):
        break
    for row in seating:
        print(row)
    print('-----')
    for row in new_seating:
        print(row)        
    print('********\n')
    seating = copy.deepcopy(new_seating)


seated_count = 0
for row in seating:
    for seat in row:    
        if seat == '#':
            seated_count += 1
print(seated_count)