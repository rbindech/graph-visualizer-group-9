import networkx as nx


def get_fundamental_cycles(graph):

  # Ensure a consistent reference order for all edges in the graph (columns)
  sorted_edges = sorted([tuple(sorted(e)) for e in graph.edges()])
  edge_to_index = {edge: i for i, edge in enumerate(sorted_edges)}

  # 1. Find a spanning tree using Depth-First Search (DFS)
  start_node = list(graph.nodes())[0]
  spanning_tree = nx.dfs_tree(graph, source=start_node)
  normalized_tree_edges = {tuple(sorted(e)) for e in spanning_tree.edges()}

  # All edges in the graph (normalized as sorted tuples)
  all_edges_set = {tuple(sorted(e)) for e in graph.edges()}

  # Chords are the non-tree edges (total edges - tree edges)
  chords = sorted(list(all_edges_set - normalized_tree_edges))

  cycles = []
  matrix = []

  # 2. For each chord, construct its fundamental cycle
  for chord in chords:
    u, v = chord
    # Find the unique path in the spanning tree between the chord's endpoints
    tree_path = nx.shortest_path(spanning_tree, source=u, target=v)

    # Convert the path nodes into a list of edges
    cycle_edges = []
    for i in range(len(tree_path) - 1):
      edge = tuple(sorted((tree_path[i], tree_path[i + 1])))
      cycle_edges.append(edge)

    # Add the chord itself to close the fundamental cycle
    chord_normalized = tuple(sorted(chord))
    cycle_edges.append(chord_normalized)

    cycles.append(cycle_edges)

    # 3. Build the corresponding binary row for the cycle matrix
    row = [0] * len(sorted_edges)
    for edge in cycle_edges:
      if edge in edge_to_index:
        row[edge_to_index[edge]] = 1
    matrix.append(row)
#
  return cycles, matrix, sorted_edges