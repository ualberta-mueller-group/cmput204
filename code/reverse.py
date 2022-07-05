def reverse(graph):
    rGraph = {}
    for node in graph:
        rGraph[node] = [] # initialize adj. lists
    for node in graph:
        for neighbor in graph[node]:
            rGraph[neighbor].append(node)
    return rGraph
