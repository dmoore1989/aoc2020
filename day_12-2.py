file1 = open('day_12-in.txt', 'r')
lines = file1.readlines()
ordinality = {
    0: (0,1),
    90: (1,0),
    180: (0,-1),
    270: (-1, 0)
}
cardinality = {
    'N': 0,
    'E': 90,
    'S': 180,
    'W': 270
}
ship_facing = 90
ship_pos = [0,0]
waypoint = [10, 1]
for line in lines:
    instruction = line[0]
    number = int(line[1:])
    if instruction  == 'F':
        ship_pos_x = ship_pos[0] + waypoint[0] * number
        ship_pos_y = ship_pos[1] + waypoint[1] * number
        ship_pos = [ship_pos_x, ship_pos_y]
    elif instruction == 'R':
        if number == 90:
            waypoint = [waypoint[1], -waypoint[0]]
        elif number == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        elif number == 270:
            waypoint = [-waypoint[1], waypoint[0]]
    elif instruction == 'L':
        if number == 90:
            waypoint = [-waypoint[1], waypoint[0]]
        elif number == 180:
            waypoint = [-waypoint[0], -waypoint[1]]
        elif number == 270:
            waypoint = [waypoint[1], -waypoint[0]]
    else:
        direction = ordinality[cardinality[instruction]]
        waypoint_x = waypoint[0] + direction[0] * number
        waypoint_y = waypoint[1] + direction[1] * number
        waypoint = [waypoint_x, waypoint_y]
    print(instruction, number, ship_pos, ship_facing, waypoint)
print(ship_pos, abs(ship_pos[0]) + abs(ship_pos[1]))