#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:50:02 2023

@author: shyamanand
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def prim(graph, start):
    T = set()
    U = {start}
    heap = [(cost, start, v) for v, cost in graph[start].items()]
    heapq.heapify(heap)

    while U != set(graph.keys()):
        cost, u, v = heapq.heappop(heap)
        if v not in U:
            T.add((u, v))
            U.add(v)
            for neighbor, weight in graph[v].items():
                if neighbor not in U:
                    heapq.heappush(heap, (weight, v, neighbor))

    return T

def plot_graph_with_edges(graph, edges, title):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black", node_color="lightgreen", font_weight="bold", width=2)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()

graph_1 = {
    'A': {'B': 2, 'C': 4, 'D': 3},
    'B': {'A': 2, 'C': 1, 'D': 4},
    'C': {'A': 4, 'B': 1, 'D': 2},
    'D': {'A': 3, 'B': 4, 'C': 2}
}

graph_2 = {
    '1': {'2': 1, '3': 2},
    '2': {'1': 1, '3': 3},
    '3': {'1': 2, '2': 3}
}

graph_3 = {
    'X': {'Y': 2, 'Z': 1, 'W': 3},
    'Y': {'X': 2, 'Z': 3, 'W': 1},
    'Z': {'X': 1, 'Y': 3, 'W': 2},
    'W': {'X': 3, 'Y': 1, 'Z': 2}
}

graph_4 = {
    'M': {'N': 2, 'O': 3, 'P': 1},
    'N': {'M': 2, 'O': 1, 'P': 4},
    'O': {'M': 3, 'N': 1, 'P': 2},
    'P': {'M': 1, 'N': 4, 'O': 2}
}


print("AS ARROWS ARE NOT HIGHLIGHTED IN THE PLOT, CHECK KERNEL FOR THE TRAVELLING OF THE SHORTEST PATH DISTANCE.")
# Run Prim's algorithm on Sample Graphs, print the resulting minimum spanning tree, and plot the graphs
start_node = list(graph_1.keys())[0]
min_spanning_tree_1 = prim(graph_1, start_node)
print("Minimum Spanning Tree (Prim) - Sample Case 1:")
print(min_spanning_tree_1)
plot_graph_with_edges(graph_1, min_spanning_tree_1, "Minimum Spanning Tree (Prim) - Sample Case 1")

start_node = list(graph_2.keys())[0]
min_spanning_tree_2 = prim(graph_2, start_node)
print("\nMinimum Spanning Tree (Prim) - Sample Case 2:")
print(min_spanning_tree_2)
plot_graph_with_edges(graph_2, min_spanning_tree_2, "Minimum Spanning Tree (Prim) - Sample Case 2")

start_node = list(graph_3.keys())[0]
min_spanning_tree_3 = prim(graph_3, start_node)
print("\nMinimum Spanning Tree (Prim) - Sample Case 3:")
print(min_spanning_tree_3)
plot_graph_with_edges(graph_3, min_spanning_tree_3, "Minimum Spanning Tree (Prim) - Sample Case 3")

start_node = list(graph_4.keys())[0]
min_spanning_tree_4 = prim(graph_4, start_node)
print("\nMinimum Spanning Tree (Prim) - Sample Case 4:")
print(min_spanning_tree_4)
plot_graph_with_edges(graph_4, min_spanning_tree_4, "Minimum Spanning Tree (Prim) - Sample Case 4")

