
pos = 50
count = 0

with open("day_1/input.txt") as f:
    for line in f:
        sign = -1 if line[0] == "L" else 1
        delta = int(line[1:])
        for i in range(delta):
            pos += sign
            if pos % 100 == 0:
                count += 1

print(count)