#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:40:01 2023

@author: shyamanand
"""
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Use DiGraph for directed edges

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def floyd_warshall_verbose(graph):
    num_nodes = len(graph.nodes)
    distances = {node: {other_node: float('infinity') for other_node in graph.nodes} for node in graph.nodes}
    next_nodes = {node: {other_node: None for other_node in graph.nodes} for node in graph.nodes}

    for node in graph.nodes:
        distances[node][node] = 0
        for neighbor, edge_data in graph[node].items():
            distances[node][neighbor] = edge_data['weight']
            next_nodes[node][neighbor] = neighbor

    for k in graph.nodes:
        for i in graph.nodes:
            for j in graph.nodes:
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
                    next_nodes[i][j] = next_nodes[i][k]

    return distances, next_nodes

def print_shortest_path(node_i, node_j, next_nodes):
    path = [node_i]
    while node_i != node_j:
        node_i = next_nodes[node_i][node_j]
        path.append(node_i)
    return path

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

# Test Case for Floyd-Warshall with a larger graph
graph_fw_large = Graph()
graph_fw_large.add_node("A")
graph_fw_large.add_node("B")
graph_fw_large.add_node("C")
graph_fw_large.add_node("D")
graph_fw_large.add_node("E")

graph_fw_large.add_edge("A", "B", 3)
graph_fw_large.add_edge("A", "C", 7)
graph_fw_large.add_edge("B", "C", 2)
graph_fw_large.add_edge("B", "D", 5)
graph_fw_large.add_edge("C", "D", 1)
graph_fw_large.add_edge("D", "E", 8)
graph_fw_large.add_edge("E", "A", 2)

print("Floyd-Warshall Algorithm (Larger Graph):")
visualize_graph(graph_fw_large)
shortest_distances_fw_large, next_nodes_fw_large = floyd_warshall_verbose(graph_fw_large.graph)
print("Shortest Distances Matrix:")
for node in graph_fw_large.graph.nodes:
    print(f"{node}: {shortest_distances_fw_large[node]}")

# Example of printing the shortest path from 'A' to 'E'
start_node = 'A'
end_node = 'E'
path_A_to_E = print_shortest_path(start_node, end_node, next_nodes_fw_large)
print(f"Shortest Path from {start_node} to {end_node}: {path_A_to_E}")
