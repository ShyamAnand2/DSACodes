#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:18:05 2023

@author: shyamanand
"""
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Sample Graphs
graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

graph_2 = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2'],
    '5': ['2'],
    '6': ['3'],
    '7': ['3']
}

graph_3 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'W'],
    'Z': ['X'],
    'W': ['Y']
}

graph_4 = {
    'M': ['N', 'O'],
    'N': ['O'],
    'O': []
}

def plot_graph(graph, title):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="black", node_color="skyblue", font_weight="bold", width=2)
    plt.title(title)
    plt.show()

# Run BFS on Sample Graphs and Plot
print("Sample Case 1:")
bfs(graph_1, 'A')
plot_graph(graph_1, "Sample Case 1 - BFS")

print("\nSample Case 2:")
bfs(graph_2, '1')
plot_graph(graph_2, "Sample Case 2 - BFS")

print("\nSample Case 3:")
bfs(graph_3, 'X')
plot_graph(graph_3, "Sample Case 3 - BFS")

print("\nSample Case 4:")
bfs(graph_4, 'M')
plot_graph(graph_4, "Sample Case 4 - BFS")
