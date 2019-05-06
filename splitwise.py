#!/usr/bin/env python

class Graph:
    def __init__(self, nodes, edges, weights):
        self.nodes = nodes
        self.edges = edges
        self.weights = weights

def splitwise(graph):
    # Step 1: Find the "net weight" of every node
    net_weights = {node: 0 for node in graph.nodes}
    for i, edge in enumerate(graph.edges):
        net_weights[edge[0]] += graph.weights[i]
        net_weights[edge[1]] -= graph.weights[i]

    # Step 2: Sort from most in-debt to least.
    nodes = sorted(graph.nodes,
        key=lambda n: net_weights[n], reverse=True)

    # Step 3: Greedy match up nodes at either extreme end of the
    # list.
    i = 0
    j = len(nodes) - 1
    amount = 0
    result = []
    # while i <= j:
    #     if amount > 0:
    #         j -= 1
    #         result.append((nodes[i], nodes[j], ))
