def islandcount(grid):

    visited = {}
    count = 0

    for r in range(0, len(grid)):
        for c in range(0, len(grid[0])):
            if explore(grid, r, c, visited) == True:
                count += 1

    return count


def explore(grid, r, c, visited):
    if not((r >= 0) and (r < len(grid))):
        return False
    if not((c >= 0) and (c < len(grid[0]))):
        return False

    if grid[r][c] == 'W':
        return False

    pos = str(r) + ',' + str(c)

    if pos in visited.keys():
        return False
    visited[pos] = True

    explore(grid, r - 1, c, visited)
    explore(grid, r + 1, c, visited)
    explore(grid, r, c - 1, visited)
    explore(grid, r, c + 1, visited)

    return True


grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print(islandcount(grid))