
timeline_end = {}

with open("day_7/input.txt") as f:
    for i, line in enumerate(f):
        if i == 0:
            timeline_end = {line.index("S") : 1}
            continue
        for beam in timeline_end.copy():
            if timeline_end[beam] == 0:
                continue

            if line[beam] == "^":
                num = timeline_end[beam]
                timeline_end[beam] = 0

                if beam != 0:
                    timeline_end[beam - 1] = timeline_end.get(beam-1, 0) + num
                if beam != len(line.strip()) - 1:
                    timeline_end[beam + 1] = timeline_end.get(beam+1, 0) + num

print(sum(timeline_end.values()))
