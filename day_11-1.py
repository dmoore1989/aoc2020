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
        if y_index + seating_neighbor[0] == len(seating) or y_index + seating_neighbor[0] < 0:
            continue
        row = seating[y_index + seating_neighbor[0]]
        if (x_index + seating_neighbor[1] != len(row) and x_index + seating_neighbor[1] >= 0) and row[x_index + seating_neighbor[1]] == '#':
            return False
    return True

def should_be_emptied(x_index, y_index, seating):
    seats_full = 0
    for seating_neighbor in seating_neighbors:
        if y_index + seating_neighbor[0] == len(seating) or y_index + seating_neighbor[0] < 0:
            continue
        row = seating[y_index + seating_neighbor[0]]
        if (x_index + seating_neighbor[1] != len(row) and x_index + seating_neighbor[1] >= 0) and row[x_index + seating_neighbor[1]] == '#':
            seats_full += 1
    return seats_full >= 4

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
    seating = copy.deepcopy(new_seating)


seated_count = 0
for row in seating:
    for seat in row:    
        if seat == '#':
            seated_count += 1
print(seated_count)