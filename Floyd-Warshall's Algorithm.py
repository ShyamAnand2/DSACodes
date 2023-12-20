#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:09:11 2023

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

def print_final_result(result, graph_name):
    print(f"Final Result for {graph_name}:\n", result)
    print("\n\n")

def draw_graph(graph, pos, edge_labels, title):
    nx.draw(graph, pos, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="skyblue", font_weight="bold", width=2, arrows=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    plt.title(title)
    plt.show()

simple_graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2}, 'C': {'A': 4, 'B': 2}}
vertices_1 = sorted(simple_graph)
simple_graph_matrix = [[simple_graph.get(u, {}).get(v, np.inf) for v in vertices_1] for u in vertices_1]
result_1 = floyd_warshall(simple_graph_matrix)
print_final_result(result_1, "Simple Graph")

G1 = nx.DiGraph(simple_graph)
pos1 = nx.spring_layout(G1)
draw_graph(G1, pos1, nx.get_edge_attributes(G1, 'weight'), "Simple Graph (Floyd-Warshall Shortest Paths)")

medium_graph = {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1, 'D': 3}, 'C': {'A': 5, 'B': 1, 'D': 2}, 'D': {'B': 3, 'C': 2}}
vertices_2 = sorted(medium_graph)
medium_graph_matrix = [[medium_graph.get(u, {}).get(v, np.inf) for v in vertices_2] for u in vertices_2]
result_2 = floyd_warshall(medium_graph_matrix)
print_final_result(result_2, "Medium Complexity Graph")

G2 = nx.DiGraph(medium_graph)
pos2 = nx.spring_layout(G2)
draw_graph(G2, pos2, nx.get_edge_attributes(G2, 'weight'), "Medium Complexity Graph (Floyd-Warshall Shortest Paths)")

complex_graph = {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1, 'D': 3, 'E': 6}, 'C': {'A': 5, 'B': 1, 'D': 2}, 'D': {'B': 3, 'C': 2, 'E': 4}, 'E': {'B': 6, 'D': 4, 'F': 8}, 'F': {'E': 8}}
vertices_3 = sorted(complex_graph)
complex_graph_matrix = [[complex_graph.get(u, {}).get(v, np.inf) for v in vertices_3] for u in vertices_3]
result_3 = floyd_warshall(complex_graph_matrix)
print_final_result(result_3, "More Nodes and Edges Graph")

G3 = nx.DiGraph(complex_graph)
pos3 = nx.spring_layout(G3)
draw_graph(G3, pos3, nx.get_edge_attributes(G3, 'weight'), "More Nodes and Edges Graph (Floyd-Warshall Shortest Paths)")

directed_graph = {
    'A': {'B': 2, 'C': 5},
    'B': {'C': 1, 'D': 3},
    'C': {'D': 2},
    'D': {'A': 7} 
}
vertices_4 = sorted(directed_graph)
directed_graph_matrix = [[directed_graph.get(u, {}).get(v, np.inf) for v in vertices_4] for u in vertices_4]
result_4 = floyd_warshall(directed_graph_matrix)
print_final_result(result_4, "Directed Graph")

G4 = nx.DiGraph(directed_graph)
pos4 = nx.spring_layout(G4)
draw_graph(G4, pos4, nx.get_edge_attributes(G4, 'weight'), "Directed Graph (Floyd-Warshall Shortest Paths)")
