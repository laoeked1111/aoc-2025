
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

accessible = 0
for r in range(len(papers)):
    for c in range(len(papers[r])):
        if papers[r][c] != '@':
            continue

        adjacent = 0
        for adj_r, adj_c in adjacent_indices(papers, r, c):
            if papers[adj_r][adj_c] == '@':
                adjacent += 1
            if adjacent >= 4:
                break
        else:
            accessible += 1

print(accessible)