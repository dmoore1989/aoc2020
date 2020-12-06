file1 = open('day_5-in.txt', 'r')
Lines = file1.readlines()
max_id = 0
for line in Lines:
    row = line[0:7]
    column = line[7:10]
    row = row.replace('F', "0", 8)
    row = row.replace('B', "1", 8)
    row_int = int(row, 2)
    column = column.replace('L', "0", 8)
    column = column.replace('R', "1", 8)
    column_int = int(column, 2)
    seat_id = row_int * 8 + column_int
    if seat_id > max_id:
        max_id = seat_id

print(max_id)