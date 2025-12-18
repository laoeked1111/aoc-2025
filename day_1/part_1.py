
pos = 50
counter = 0

with open("day_1/input.txt") as f:
    for line in f:
        direction = -1 if line[0] == 'L' else 1
        pos = (pos + direction * int(line[1:])) % 100
        if pos == 0:
            counter += 1

print(counter)