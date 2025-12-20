
beams = set()
num_splits = 0

with open("day_7/input.txt") as f:
    for i, line in enumerate(f):
        if i == 0:
            beams.add(line.index("S"))
            continue
        for beam in beams.copy():
            if line[beam] == "^":
                beams.remove(beam)
                num_splits += 1

                if beam != 0:
                    beams.add(beam - 1)
                if beam != len(line.strip()) - 1:
                    beams.add(beam + 1)

print(num_splits)
