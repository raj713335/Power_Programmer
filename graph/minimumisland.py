import math


def minimumisland(grid):

    visited = {}
    min_size = math.inf

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            size = exploreSize(grid, r, c, visited)
            if (size > 0) and (min_size > size):
                min_size = size

    return min_size


def exploreSize(grid, r, c, visited):
    if not((r >= 0) and (r < len(grid))):
        return 0
    if not((c >= 0) and (c < len(grid[0]))):
        return 0

    if grid[r][c] == 'W':
        return 0

    pos = str(r) + ',' + str(c)

    if pos in visited.keys():
        return 0
    visited[pos] = True

    size = 1
    size += exploreSize(grid, r - 1, c, visited)
    size += exploreSize(grid, r + 1, c, visited)
    size += exploreSize(grid, r, c - 1, visited)
    size += exploreSize(grid, r, c + 1, visited)

    return size


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print(minimumisland(grid))