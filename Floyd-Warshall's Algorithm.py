#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:40:01 2023

@author: shyamanand
"""
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def floyd_warshall(graph):
    V = len(graph)
    distance_matrix = np.full((V, V), np.inf)
    
    for i, row in enumerate(graph):
        for j, weight in enumerate(row):
            distance_matrix[i, j] = weight

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if distance_matrix[i, k] + distance_matrix[k, j] < distance_matrix[i, j]:
                    distance_matrix[i, j] = distance_matrix[i, k] + distance_matrix[k, j]

    return distance_matrix

def draw_directed_graph(graph, pos, edge_labels, title):
    plt.figure(figsize=(8, 6))
    nx.draw(graph, pos, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="gold", font_weight="bold", width=2)

    # Draw edges with arrowheads and edge labels
    for edge, weight in edge_labels.items():
        nx.draw_networkx_edges(graph, pos, edgelist=[edge], width=2, edge_color='black', connectionstyle='arc3,rad=0.1', arrowsize=15, arrowstyle='->')
        nx.draw_networkx_edge_labels(graph, pos, edge_labels={(edge[0], edge[1]): weight}, font_color='red')

    plt.title(title)
    plt.show()

# Sample directed graphs (all directed)
simple_directed_graph = {'A': {'B': 2, 'C': 5, 'D': 1}, 'B': {'C': 1, 'D': 3}, 'C': {'D': 2}, 'D': {'A': 7}}
medium_directed_graph = {'X': {'Y': 2, 'Z': 5}, 'Y': {'Z': 1, 'W': 3}, 'Z': {'W': 2}, 'W': {'X': 7}}
complex_directed_graph = {'M': {'N': 2, 'O': 5}, 'N': {'O': 1, 'P': 3}, 'O': {'P': 2}, 'P': {'M': 7}}

# Floyd-Warshall results
vertices = sorted(simple_directed_graph)
simple_directed_matrix = [[simple_directed_graph.get(u, {}).get(v, np.inf) for v in vertices] for u in vertices]
result_simple_directed = floyd_warshall(simple_directed_matrix)
print("Result:\n", result_simple_directed)
print("\n\n")

vertices = sorted(medium_directed_graph)
medium_directed_matrix = [[medium_directed_graph.get(u, {}).get(v, np.inf) for v in vertices] for u in vertices]
result_medium_directed = floyd_warshall(medium_directed_matrix)
print("Result:\n", result_medium_directed)
print("\n\n")

vertices = sorted(complex_directed_graph)
complex_directed_matrix = [[complex_directed_graph.get(u, {}).get(v, np.inf) for v in vertices] for u in vertices]
result_complex_directed = floyd_warshall(complex_directed_matrix)
print("Result:\n", result_complex_directed)
print("\n\n")

# Draw directed graphs with arrows and edge labels
G_simple_directed = nx.DiGraph(simple_directed_graph)
pos_simple_directed = nx.spring_layout(G_simple_directed)
draw_directed_graph(G_simple_directed, pos_simple_directed, nx.get_edge_attributes(G_simple_directed, 'weight'), "Simple Directed Graph (Floyd-Warshall Shortest Paths)")

G_medium_directed = nx.DiGraph(medium_directed_graph)
pos_medium_directed = nx.spring_layout(G_medium_directed)
draw_directed_graph(G_medium_directed, pos_medium_directed, nx.get_edge_attributes(G_medium_directed, 'weight'), "Medium Directed Graph (Floyd-Warshall Shortest Paths)")

G_complex_directed = nx.DiGraph(complex_directed_graph)
pos_complex_directed = nx.spring_layout(G_complex_directed)
draw_directed_graph(G_complex_directed, pos_complex_directed, nx.get_edge_attributes(G_complex_directed, 'weight'), "Complex Directed Graph (Floyd-Warshall Shortest Paths)")
