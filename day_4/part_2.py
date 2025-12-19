
papers = []
with open("day_4/input.txt") as f:
    for line in f:
        papers += [line]

def adjacent_indices(arr, r, c):
    rows = r-1, r, r+1
    cols = c-1, c, c+1

    yield from (
        (row, col)
        for row in rows
        for col in cols
        if 0 <= row < len(arr)
        and 0 <= col < len(arr[row])
        and (row, col) != (r,c)
    )

def find_accessible(locs):
    accessible = []
    for r, c in locs:
        adjacent = 0
        for adj_r, adj_c in adjacent_indices(papers, r, c):
            if papers[adj_r][adj_c] == '@':
                adjacent += 1
            if adjacent >= 4:
                break
        else:
            accessible.append((r,c))
    return accessible

visited = {
    (r,c)
    for r in range(len(papers))
    for c in range(len(papers[r]))
    if papers[r][c] != '@'
}

paper_locs = [
    (r,c)
    for r in range(len(papers))
    for c in range(len(papers[r]))
    if (r,c) not in visited
]

queue = find_accessible(paper_locs)

removed = 0
while queue:
    this_r, this_c = queue.pop(0)
    if (this_r, this_c) in visited:
        continue

    papers[this_r] = papers[this_r][:this_c] + "." + papers[this_r][this_c+1:]

    removed += 1
    visited.add((this_r, this_c))

    adjacent_papers = list(
        idx
        for idx in adjacent_indices(papers, this_r, this_c)
        if idx not in visited
    )

    queue.extend(
        a
        for a in find_accessible(adjacent_papers)
    )

print(removed)