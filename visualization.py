import matplotlib.pyplot as plt
import networkx as nx
from graph import get_ordered_edges


def draw_graph(graph, edges_order=None, title="Graph Visualization"):
    # Use ordered edges from graph module if not provided
    if edges_order is None:
        edges_order = get_ordered_edges(graph)

    # Set fixed node layout
    pos = nx.spring_layout(graph, seed=42)

    # Map each edge to its label (e1, e2, ...)
    edge_labels = {}
    i = 1
    for edge in edges_order:
        edge_labels[edge] = "e" + str(i)
        i = i + 1

    # Draw nodes and labeled edges
    nx.draw(graph, pos, with_labels=True)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    plt.title(title)
    plt.show()


def print_matrix(matrix, row_labels, col_labels, title="Matrix"):
    print("\n=== " + title + " ===")

    # Print column header
    header = "\t"
    for col in col_labels:
        header = header + str(col) + "\t"
    print(header)

    # Print each row with its label
    for i in range(len(matrix)):
        row_str = str(row_labels[i]) + "\t"
        for val in matrix[i]:
            row_str = row_str + str(val) + "\t"
        print(row_str)
    print()
