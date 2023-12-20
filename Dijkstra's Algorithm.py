#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:18:45 2023

@author: shyamanand
"""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, source):
    visited = set()
    distance = {vertex: float('infinity') for vertex in graph}
    distance[source] = 0
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            distance_through_current = current_distance + weight

            if distance_through_current < distance[neighbor]:
                distance[neighbor] = distance_through_current
                heapq.heappush(priority_queue, (distance_through_current, neighbor))

    return distance

simple_graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2}, 'C': {'A': 4, 'B': 2}}
source_vertex_1 = 'B'
result_1 = dijkstra(simple_graph, source_vertex_1)
print(f"Shortest distances from {source_vertex_1}: {result_1}")
print("\n\n")

G1 = nx.Graph(simple_graph)
pos1 = nx.spring_layout(G1)
nx.draw(G1, pos1, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="skyblue", font_weight="bold", width=2)
labels1 = nx.get_edge_attributes(G1, 'weight')
nx.draw_networkx_edge_labels(G1, pos1, edge_labels=labels1)
plt.title(f"Simple Graph (Dijkstra's Shortest Path from {source_vertex_1})")
plt.show()

medium_graph = {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1, 'D': 3}, 'C': {'A': 5, 'B': 1, 'D': 2}, 'D': {'B': 3, 'C': 2}}
source_vertex_2 = 'C'
result_2 = dijkstra(medium_graph, source_vertex_2)
print(f"Shortest distances from {source_vertex_2}: {result_2}")
print("\n\n")

G2 = nx.Graph(medium_graph)
pos2 = nx.spring_layout(G2)
nx.draw(G2, pos2, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="lightcoral", font_weight="bold", width=2)
labels2 = nx.get_edge_attributes(G2, 'weight')
nx.draw_networkx_edge_labels(G2, pos2, edge_labels=labels2)
plt.title(f"Medium Complexity Graph (Dijkstra's Shortest Path from {source_vertex_2})")
plt.show()

complex_graph = {'A': {'B': 2, 'C': 5}, 'B': {'A': 2, 'C': 1, 'D': 3, 'E': 6}, 'C': {'A': 5, 'B': 1, 'D': 2}, 'D': {'B': 3, 'C': 2, 'E': 4}, 'E': {'B': 6, 'D': 4, 'F': 8}, 'F': {'E': 8}}
source_vertex_3 = 'A'
result_3 = dijkstra(complex_graph, source_vertex_3)
print(f"Shortest distances from {source_vertex_3}: {result_3}")
print("\n\n")

G3 = nx.Graph(complex_graph)
pos3 = nx.spring_layout(G3)
nx.draw(G3, pos3, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="lightgreen", font_weight="bold", width=2)
labels3 = nx.get_edge_attributes(G3, 'weight')
nx.draw_networkx_edge_labels(G3, pos3, edge_labels=labels3)
plt.title(f"More Nodes and Edges Graph (Dijkstra's Shortest Path from {source_vertex_3})")
plt.show()

directed_graph = {'A': {'B': 2, 'C': 5}, 'B': {'C': 1, 'D': 3}, 'C': {'D': 2}, 'D': {}}
source_vertex_4 = 'D'
result_4 = dijkstra(directed_graph, source_vertex_4)
print(f"Shortest distances from {source_vertex_4}: {result_4}")
print("\n\n")


G4 = nx.DiGraph(directed_graph)
pos4 = nx.spring_layout(G4)
nx.draw(G4, pos4, with_labels=True, node_size=700, font_size=10, font_color="white", node_color="gold", font_weight="bold", width=2)
labels4 = nx.get_edge_attributes(G4, 'weight')
nx.draw_networkx_edge_labels(G4, pos4, edge_labels=labels4)
plt.title(f"Directed Graph (Dijkstra's Shortest Path from {source_vertex_4})")
plt.show()
