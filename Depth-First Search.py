#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:33:35 2023

@author: shyamanand
"""

import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Sample Graphs
graph_1 = {
    'A': ['D'],
    'B': ['A'],
    'C': ['B'],
    'D': ['E'],
    'E': ['F'],
    'F': ['G'],
    'G': ['C']
}

graph_2 = {
    '1': ['2', '6', '7'],
    '2': ['4'],
    '3': ['5'],
    '4': ['3'],
    '5': ['2', '3'],
    '6': [],
    '7': ['4', '6']
}

graph_3 = {
    'X': ['W'],
    'Y': [],
    'Z': ['X'],
    'W': ['Y']
}

graph_4 = {
    'M': ['N', 'O'],
    'N': ['O'],
    'O': []
}

def plot_graph(graph, title):
    G = nx.DiGraph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black", node_color="lightcoral", font_weight="bold", width=2)
    plt.title(title)
    plt.show()

# Run DFS on Sample Graphs and Plot
print("Sample Case 1:")
dfs(graph_1, 'C')
plot_graph(graph_1, "Sample Case 1 - DFS")

print("\nSample Case 2:")
dfs(graph_2, '5')
plot_graph(graph_2, "Sample Case 2 - DFS")

print("\nSample Case 3:")
dfs(graph_3, 'W')
plot_graph(graph_3, "Sample Case 3 - DFS")

print("\nSample Case 4:")
dfs(graph_4, 'O')
plot_graph(graph_4, "Sample Case 4 - DFS")
