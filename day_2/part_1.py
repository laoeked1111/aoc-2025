
with open("day_2/input.txt") as f:
    for line in f:
        pass
ranges = line.strip().split(',')

num_ranges = []
for this_range in ranges:
    nums = this_range.split('-')
    num_ranges.append(
        (int(nums[0]), int(nums[1]))
    )

invalid_ids = []
for low, high in num_ranges:
    for i in range(low, high + 1):
        str_num = str(i)
        l = len(str_num)
        if l % 2 == 1:
            continue

        if str_num == str_num[:l//2] * 2:
            invalid_ids.append(i)

print(sum(invalid_ids))