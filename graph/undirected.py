def undirected(edges, nodeA, nodeB):
    graph = build_graph(edges)
    return hasPath(graph, nodeA, nodeB, {})


def hasPath(graph, src, dst, visited):
    if src == dst:
        return True

    if src in visited.keys():
        return False

    visited[src] = True

    for neighbour in graph[src]:
        if hasPath(graph, neighbour, dst, visited) ==  True:
            return True

    return False




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
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]


print(build_graph(edges=edges))
print(undirected(edges, 'j', 'm'))
