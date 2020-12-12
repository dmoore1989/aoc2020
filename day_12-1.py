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
for line in lines:
    instruction = line[0]
    number = int(line[1:])
    if instruction == 'R':
        ship_facing = (ship_facing + number) % 360     
    elif instruction == 'L':
        ship_facing = (ship_facing - number) % 360
    else:
        if instruction  == 'F':
            direction = ordinality[ship_facing]
        else:
            direction = ordinality[cardinality[instruction]]
        ship_pos_x = ship_pos[0] + direction[0] * number
        ship_pos_y = ship_pos[1] + direction[1] * number
        ship_pos = [ship_pos_x, ship_pos_y]
    print(instruction, number, ship_pos, ship_facing)
print(ship_pos, abs(ship_pos[0]) + abs(ship_pos[1]))