
hw = []

with open("day_6/input.txt") as f:
    for line in f:
        hw.append(line.strip().split())

ops = hw.pop(-1)

tot = 0
for i in range(len(hw[0])):
    if ops[i] == '+':
        tot += sum(int(row[i]) for row in hw)
    elif ops[i] == '*':
        temp = 1
        for row in hw:
            temp *= int(row[i])
        tot += temp

print(tot)