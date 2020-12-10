import re

file_path = 'input_data.txt'

with open(file_path, 'r') as file:
    seat_map = [False for i in range(2**10)]
    max = 0
    for line in file.readlines():
        row = [i for i in range(128)]
        seat = [i for i in range(8)]
        row_code = re.search("(F|B){7}", line).group()
        seat_code = re.search("(R|L){3}", line).group()
        for c in row_code:
            row = row[:len(row)//2] if c == "F" else row[len(row)//2:]
            if len(row) <= 1:
                row_result = row[0]
                break
        for c in seat_code:
            seat = seat[:len(seat)//2] if c=="L" else seat[len(seat)//2:]
            if len(seat) <= 1:
                seat_result = seat[0]
                break

        score = row_result*8+seat_result
        seat_map[score] = True
        print("row", row_result)
        print("seat", seat_result)
        print("id", score)
        max = score if score > max else max
    print ("max", max)
    for i in range(len(seat_map)):
        if seat_map[i-1] and seat_map[i+1] and not seat_map[i]:
            print("your seat", i)