#!/usr/bin/env python


class Graph:
    def __init__(self, nodes, edges, weights):
        self.nodes = nodes
        self.edges = edges
        self.weights = weights
        assert(len(edges) == len(weights))


def splitwise(graph):
    # Step 1: Find the "net weight" of every node
    net_weights = {node: 0 for node in graph.nodes}
    for i, edge in enumerate(graph.edges):
        net_weights[edge[0]] += graph.weights[i]
        net_weights[edge[1]] -= graph.weights[i]
    assert(sum(w for w in net_weights.values()) == 0)

    # Step 2: Sort from most in-debt to least.
    nodes = sorted(graph.nodes,
                   key=lambda n: net_weights[n], reverse=True)

    # Step 3: Greedy match up nodes at either extreme end of the
    # list.
    amount = 0
    result = []
    for i in range(len(nodes)):
        node = nodes[i]
        j = len(nodes) - 1
        while net_weights[nodes[i]]:
            transfer = min(abs(net_weights[nodes[i]]), abs(
                net_weights[nodes[j]]))
            if transfer:
                net_weights[nodes[j]] += transfer
                net_weights[nodes[i]] -= transfer
                result.append((nodes[i], nodes[j], transfer))
            j -= 1

    return result


if __name__ == '__main__':
    graph = Graph([], [], [])
    assert(splitwise(graph) == [])

    graph = Graph(['a', 'b', 'c'], [('a', 'b')], [30])
    assert(splitwise(graph) == [('a', 'b', 30)])

    graph = Graph(
        ['a', 'b', 'c'],
        [('a', 'b'), ('b', 'c')],
        [30, 30],
    )
    assert(splitwise(graph) == [('a', 'c', 30)])

    graph = Graph(
        ('a', 'b', 'c', 'd'),
        (('a', 'd'), ('c', 'b'), ('d', 'c')),
        (30, 15, 15),
    )
    assert(splitwise(graph) == [('a', 'd', 15), ('a', 'b', 15)])
