
fresh_ids = []
available_ids = []

with open("day_5/input.txt") as f:
    fresh_flag = True

    for line in f:
        if line == '\n':
            fresh_flag = False
            continue

        if fresh_flag:
            low, high = line.strip().split('-')
            fresh_ids.append((int(low), int(high)))

        else:
            available_ids.append(int(line))

fresh_ids.sort()

i = 0
while  i < len(fresh_ids):
    this_range = fresh_ids[i]

    if i > 0:
        prev_range = fresh_ids[i-1]
        if prev_range[0] <= this_range[0] <= prev_range[1]:
            fresh_ids[i-1] = prev_range[0], max(prev_range[1], this_range[1])
            fresh_ids.pop(i)
            continue

    if i < len(fresh_ids) - 1:
        next_range = fresh_ids[i+1]
        if next_range[0] <= this_range[1] <= next_range[1]:
            fresh_ids[i] = min(this_range[0], next_range[0]), next_range[1]
            fresh_ids.pop(i+1)
            continue

    i += 1

print(fresh_ids)