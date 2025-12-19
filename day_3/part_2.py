
joltages = []

def get_max_joltage(bank):
    to_remove = len(bank) - 12

    keep = []
    for i, digit in enumerate(bank):
        while to_remove > 0 and keep and int(digit) > int(keep[-1]):
            to_remove -= 1
            keep.pop()
        keep.append(digit)
    return int("".join(keep[:12]))

with open("day_3/input.txt") as f:
    for line in f:
        joltages.append(get_max_joltage(line.strip()))

print(sum(joltages))