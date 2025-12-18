
joltages = []

def get_max_joltage(battery):
    def _generate_joltages():
        for i in range(len(battery)):
            for j in range(i+1, len(battery)):
                yield int(battery[i] + battery[j])

    curr_max = int(battery[:2])
    for joltage in _generate_joltages():
        if joltage > curr_max:
            curr_max = joltage
    return curr_max

with open("day_3/input.txt") as f:
    for line in f:
        joltages.append(get_max_joltage(line))

print(sum(joltages))