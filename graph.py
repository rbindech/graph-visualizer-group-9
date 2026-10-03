import networkx as nx


def adjacency_to_graph(matrix):
    """
    Convert an adjacency matrix into an undirected NetworkX graph.

    Example:

        0 1 1
        1 0 1
        1 1 0

    becomes:

        vertices = 0, 1, 2
        edges = (0,1), (0,2), (1,2)

    Parameters:
        matrix (list[list[int]]): adjacency matrix

    Returns:
        nx.Graph: corresponding graph
    """

    graph = nx.Graph()

    number_of_vertices = len(matrix)

    # Add all vertices, even isolated ones
    graph.add_nodes_from(range(number_of_vertices))

    # Only look at the upper half of the matrix
    # because the graph is undirected.
    for i in range(number_of_vertices):
        for j in range(i + 1, number_of_vertices):

            if matrix[i][j] == 1:
                graph.add_edge(i, j)

    return graph


def incidence_to_graph(matrix):
    """
    Convert an incidence matrix into an undirected NetworkX graph.

    Rows represent vertices.
    Columns represent edges.

    Example:

            e0 e1 e2

        0    1  1  0
        1    1  0  1
        2    0  1  1

    becomes:

        edges:
        (0,1)
        (0,2)
        (1,2)

    Parameters:
        matrix (list[list[int]]): incidence matrix

    Returns:
        nx.Graph: corresponding graph
    """

    graph = nx.Graph()

    number_of_vertices = len(matrix)
    number_of_edges = len(matrix[0])

    graph.add_nodes_from(range(number_of_vertices))

    # Examine each column.
    # Each column represents one edge.
    for column in range(number_of_edges):

        incident_vertices = []

        for vertex in range(number_of_vertices):

            if matrix[vertex][column] == 1:
                incident_vertices.append(vertex)

        # Normally already checked by input_parser,
        # but this keeps graph.py safe if used independently.
        if len(incident_vertices) != 2:
            raise ValueError(
                f"Invalid incidence matrix: edge {column} "
                "must connect exactly two vertices."
            )

        u = incident_vertices[0]
        v = incident_vertices[1]

        graph.add_edge(u, v)

    return graph


def find_spanning_tree(graph, start_node=0):
    """
    Find a spanning tree using Depth-First Search (DFS).

    The spanning tree:
    - contains all vertices of the graph
    - keeps the graph connected
    - contains no cycle

    Parameters:
        graph (nx.Graph): original graph
        start_node (int): vertex from which DFS starts

    Returns:
        nx.Graph: spanning tree
    """

    if graph.number_of_nodes() == 0:
        raise ValueError("Cannot create a spanning tree from an empty graph.")

    if not nx.is_connected(graph):
        raise ValueError(
            "A spanning tree cannot be created because the graph is disconnected."
        )

    if start_node not in graph.nodes:
        raise ValueError(
            f"Start node {start_node} does not exist in the graph."
        )

    spanning_tree = nx.Graph()

    # Keep all vertices
    spanning_tree.add_nodes_from(graph.nodes)

    visited = set()

    def dfs(current_vertex):
        visited.add(current_vertex)

        # sorted() makes the result deterministic:
        # the same graph gives the same spanning tree.
        for neighbour in sorted(graph.neighbors(current_vertex)):

            if neighbour not in visited:

                spanning_tree.add_edge(
                    current_vertex,
                    neighbour
                )

                dfs(neighbour)

    dfs(start_node)

    return spanning_tree


def get_ordered_edges(graph):
    """
    Return the graph edges in a deterministic order.

    This is useful because the columns of:
    - the fundamental cycle matrix
    - the cut-set matrix

    must always correspond to the same edge order.

    Example:

        [(0, 1), (0, 2), (1, 2)]

    instead of an unpredictable order.
    """

    edges = []

    for u, v in graph.edges():

        # Because the graph is undirected,
        # (0, 2) and (2, 0) represent the same edge.
        edge = tuple(sorted((u, v)))

        edges.append(edge)

    return sorted(edges)


def print_graph_info(graph):
    """
    Utility function to display the vertices and edges of a graph.
    """

    print("\nVertices:")
    print(list(graph.nodes))

    print("\nEdges:")

    edges = get_ordered_edges(graph)

    for index, edge in enumerate(edges, start=1):
        print(f"e{index}: {edge[0]} - {edge[1]}")