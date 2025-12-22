
points = []
distances = {}

with open("day_8/input.txt") as f:
    for line in f:
        points.append(
            tuple(int(e) for e in line.strip().split(','))
        )

num_connections = 1000
points_connected = []

def calc_dist(p1, p2):
    assert len(p1) == len(p2)

    tot = 0
    for i in range(len(p1)):
        tot += (p1[i] - p2[i]) ** 2
    
    return tot ** 0.5

for i, p1 in enumerate(points):
    for p2 in points[i+1:]:
        this_dist = calc_dist(p1, p2)
        points_connected.append((this_dist, p1, p2))

points_connected.sort()
while len(points_connected) > num_connections:
    points_connected.pop()

print(points_connected)

circuits = {p:0 for p in points}

connections = 0
new_set = 1


def connect_circuits(c1, c2):
    for k, v in circuits.items():
        if v == c2:
            circuits[k] = c1

for _, p1, p2 in points_connected:
    if circuits[p1] == 0 and circuits[p2] == 0:
        circuits[p1] = new_set
        circuits[p2] = new_set
        new_set += 1

    elif circuits[p1] == 0:
        circuits[p1] = circuits[p2]

    elif circuits[p2] == 0:
        circuits[p2] = circuits[p1]

    else:
        connect_circuits(circuits[p1], circuits[p2])

circuit_sizes = {}
for v in circuits.values():
    circuit_sizes[v] = circuit_sizes.get(v, 0) + 1

sizes = [v for k,v in circuit_sizes.items() if k != 0]
sizes.sort(reverse=True)

print(sizes[0] * sizes[1] * sizes[2])
