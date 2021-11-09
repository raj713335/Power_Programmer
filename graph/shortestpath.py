def shortestPath(edges, nodeA, nodeB):
    graph = build_graph(edges)

    visited = {nodeA: True}

    queue = [[nodeA, 0]]

    while len(queue) > 0:
        # print(queue.pop())
        [node, distance] = queue.pop()
        print(node, distance)

        if node == nodeB:
            return distance

        for neighbour in graph[node]:
            print(neighbour)
            if neighbour not in visited.keys():
                visited[neighbour] = True
                queue.insert(0, [neighbour, distance+1])

    return -1



def build_graph(edges):
    graph = {}
    for edge in edges:
        a, b = edge
        if a not in graph.keys():
            graph[a] = []
        if b not in graph.keys():
            graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]


print(shortestPath(edges, 'w', 'z'))