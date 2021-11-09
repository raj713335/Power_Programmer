


def DepthFirstSearch(graph, source):

    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)

def DepthFirstSearchR(graph, source):
    print(source)
    for neighbour in graph[source]:
        DepthFirstSearchR(graph, neighbour)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

DepthFirstSearchR(graph, 'a')