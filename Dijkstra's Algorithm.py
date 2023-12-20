#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:18:45 2023

@author: shyamanand
"""

import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph.nodes}
    prev_nodes = {node: None for node in graph.nodes}
    dist[start] = 0

    unvisited_nodes = set(graph.nodes)

    while unvisited_nodes:
        curr_node = min(unvisited_nodes, key=lambda node: dist[node])
        unvisited_nodes.remove(curr_node)

        for neighbor, edge_data in graph[curr_node].items():
            dist_to_neighbor = dist[curr_node] + edge_data['weight']
            if dist_to_neighbor < dist[neighbor]:
                dist[neighbor] = dist_to_neighbor
                prev_nodes[neighbor] = curr_node

    return dist, prev_nodes

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph)
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

# Test Case 1
g1 = Graph()
g1.add_node("A")
g1.add_node("B")
g1.add_node("C")
g1.add_edge("A", "B", 2)
g1.add_edge("B", "C", 1)
g1.add_edge("A", "C", 4)
print("Test Case 1:")
visualize_graph(g1)
d1, p1 = dijkstra(g1.graph, "A")
print("Shortest Distances from A:", d1)
print("Previous Nodes:", p1)
print()

# Test Case 2
g2 = Graph()
g2.add_node("A")
g2.add_node("B")
g2.add_node("C")
g2.add_node("D")
g2.add_edge("A", "B", 1)
g2.add_edge("B", "C", 2)
g2.add_edge("C", "D", 1)
g2.add_edge("A", "C", 4)
g2.add_edge("B", "D", 7)
print("Test Case 2:")
visualize_graph(g2)
d2, p2 = dijkstra(g2.graph, "A")
print("Shortest Distances from A:", d2)
print("Previous Nodes:", p2)
print()

# Test Case 3
g3 = Graph()
g3.add_node("A")
g3.add_node("B")
g3.add_node("C")
g3.add_node("D")
g3.add_edge("A", "B", 3)
g3.add_edge("B", "C", 1)
g3.add_edge("C", "D", 5)
g3.add_edge("A", "C", 2)
g3.add_edge("B", "D", 2)
print("Test Case 3:")
visualize_graph(g3)
d3, p3 = dijkstra(g3.graph, "A")
print("Shortest Distances from A:", d3)
print("Previous Nodes:", p3)
