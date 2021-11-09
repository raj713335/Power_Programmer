def largestComponent(graph):
    visited = {}
    longest = 0
    for node in graph:
        size = exploreSize(graph, node, visited)
        if size > longest:
            longest = size

    return longest


def exploreSize(graph, current, visited):

    if current in visited.keys():
        return 0

    visited[current] = True

    size = 1

    for neighbor in graph[current]:
        size += exploreSize(graph, neighbor, visited)

    return size


print(largestComponent({
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}))