
joltages = []

def get_max_joltage(bank):
    def _generate_joltages():
        for i in range(len(bank)):
            for j in range(i+1, len(bank)):
                yield int(bank[i] + bank[j])

    curr_max = int(bank[:2])
    for joltage in _generate_joltages():
        if joltage > curr_max:
            curr_max = joltage
    return curr_max

with open("day_3/input.txt") as f:
    for line in f:
        joltages.append(get_max_joltage(line))

print(sum(joltages))