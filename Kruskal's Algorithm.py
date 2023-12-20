#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:51:14 2023

@author: shyamanand
"""

import networkx as nx
import matplotlib.pyplot as plt

class DisjointSet:
    def __init__(self, vertices):
        self.parent = {vertex: vertex for vertex in vertices}
        self.rank = {vertex: 0 for vertex in vertices}

    def find(self, vertex):
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]

    def union(self, root1, root2):
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            self.parent[root1] = root2
            self.rank[root2] += 1

def kruskal(graph):
    edges = [(u, v, weight) for u in graph for v, weight in graph[u].items()]
    edges.sort(key=lambda edge: edge[2])
    
    vertices = set(vertex for edge in edges for vertex in edge[:2])
    disjoint_set = DisjointSet(vertices)
    
    minimum_spanning_tree = set()
    for edge in edges:
        u, v, weight = edge
        root1 = disjoint_set.find(u)
        root2 = disjoint_set.find(v)
        
        if root1 != root2:
            minimum_spanning_tree.add((u, v, weight))
            disjoint_set.union(root1, root2)
    
    return minimum_spanning_tree

def plot_graph_with_edges(graph, edges, title):
    G = nx.Graph(graph)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="skyblue", font_weight="bold", width=2, arrows=True)
    nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)
    plt.title(title)
    plt.show()

# Sample Graphs
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

# Run Kruskal's algorithm on Sample Graphs, print the resulting minimum spanning tree, and plot the graphs
min_spanning_tree_1 = kruskal(graph_1)
print("Minimum Spanning Tree (Kruskal) - Sample Case 1:")
print(min_spanning_tree_1)
plot_graph_with_edges(graph_1, [(u, v) for u, v, _ in min_spanning_tree_1], "Minimum Spanning Tree (Kruskal) - Sample Case 1")

min_spanning_tree_2 = kruskal(graph_2)
print("\nMinimum Spanning Tree (Kruskal) - Sample Case 2:")
print(min_spanning_tree_2)
plot_graph_with_edges(graph_2, [(u, v) for u, v, _ in min_spanning_tree_2], "Minimum Spanning Tree (Kruskal) - Sample Case 2")

min_spanning_tree_3 = kruskal(graph_3)
print("\nMinimum Spanning Tree (Kruskal) - Sample Case 3:")
print(min_spanning_tree_3)
plot_graph_with_edges(graph_3, [(u, v) for u, v, _ in min_spanning_tree_3], "Minimum Spanning Tree (Kruskal) - Sample Case 3")

min_spanning_tree_4 = kruskal(graph_4)
print("\nMinimum Spanning Tree (Kruskal) - Sample Case 4:")
print(min_spanning_tree_4)
plot_graph_with_edges(graph_4, [(u, v) for u, v, _ in min_spanning_tree_4], "Minimum Spanning Tree (Kruskal) - Sample Case 4")
