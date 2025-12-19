

hw = []
with open("day_6/input.txt") as f:
    for line in f:
        hw.append(line)

ops = hw.pop(-1).strip().split()

def column_has_number(idx):
    for r in hw:
        if r[idx] not in "\n ":
            return True
    return False

nums = [[]]
for i in range(len(hw[0])):
    if not column_has_number(i):
        nums.append([])
        continue

    this_num = ""
    for row in hw:
        if row[i] not in "\n ":
            this_num += row[i]
    nums[-1].append(int(this_num))

nums.pop()

def prod(*args):
    ans = 1
    for arg in args:
        ans *= arg
    return ans

tot = 0
for op, these_nums in zip(ops, nums):
    if op == "+":
        tot += sum(these_nums)
    elif op == "*":
        tot += prod(*these_nums)

print(tot)
