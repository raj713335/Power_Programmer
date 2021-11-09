


def BreadthFirstSearch(graph, source):

    stack = [source]

    while stack:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
             stack.insert(0, neighbour)

def BreadthFirstSearchR(graph, source):
    print(source)
    for neighbour in graph[source]:
        BreadthFirstSearchR(graph, neighbour)


graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}

BreadthFirstSearch(graph, 'a')