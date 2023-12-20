import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def dp_shortest_path(graph, source, destination):
    nodes = list(graph.nodes)
    costs = {node: float('inf') for node in nodes}
    costs[source] = 0

    for _ in range(len(nodes)):
        for node in nodes:
            for successor in graph.successors(node):
                cost = graph[node][successor]['weight']
                costs[successor] = min(costs[successor], cost + costs[node])

    return costs[destination]

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph)
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Dynamic Programming Algorithm - Plot representation")
    plt.show()

def print_costs(costs):
    for node, cost in costs.items():
        print(f"Cost from {node} to destination: {cost}")

# Test Case 1
g1 = Graph()
g1.add_node("A")
g1.add_node("B")
g1.add_node("C")
g1.add_node("D")
g1.add_edge("A", "B", 2)
g1.add_edge("B", "C", 1)
g1.add_edge("A", "C", 4)
g1.add_edge("C", "D", 3)
g1.add_edge("B", "D", 7)

visualize_graph(g1)
src1, dest1 = "A", "D"
cost1 = dp_shortest_path(g1.graph, src1, dest1)
print(f"Cost from {src1} to {dest1}: {cost1}")

# Additional paths
print(f"Cost from B to D: {dp_shortest_path(g1.graph, 'B', 'D')}")
print(f"Cost from C to D: {dp_shortest_path(g1.graph, 'C', 'D')}")
print(f"Cost from D to D: {dp_shortest_path(g1.graph, 'D', 'D')}")
