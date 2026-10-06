import networkx as nx


def get_fundamental_cutsets(graph):
  
  # Ensure a consistent reference order for all edges in the graph (columns)
  sorted_edges = sorted([tuple(sorted(e)) for e in graph.edges()])
  edge_to_index = {edge: i for i, edge in enumerate(sorted_edges)}

  # 1. Find a spanning tree using DFS
  start_node = list(graph.nodes())[0]
  spanning_tree = nx.dfs_tree(graph, source=start_node)
  tree_edges = sorted(list(spanning_tree.edges()))
  normalized_tree_edges = {tuple(sorted(e)) for e in tree_edges}

  all_edges_set = {tuple(sorted(e)) for e in graph.edges()}

  cutsets = []
  matrix = []

  # 2. For each tree edge, construct its fundamental cut-set
  for tree_edge in tree_edges:
    # Create a copy of the spanning tree and remove the current tree edge
    temp_tree = spanning_tree.copy()
    u, v = tree_edge
    temp_tree.remove_edge(u, v)

    # Removing a tree edge splits the tree into two connected components (subtrees)
    components = list(nx.connected_components(temp_tree.to_undirected()))
    comp1 = components[0]
    comp2 = components[1]

    # The cut-set includes the tree edge plus any graph edges bridging the two components
    normalized_tree_edge = tuple(sorted(tree_edge))
    cutset_edges = [normalized_tree_edge]

    for edge in all_edges_set:
      if edge == normalized_tree_edge:
        continue
      n1, n2 = edge
      # Check if the edge connects comp1 to comp2
      if (n1 in comp1 and n2 in comp2) or (n1 in comp2 and n2 in comp1):
        cutset_edges.append(edge)

    cutsets.append(cutset_edges)

    # 3. Build the corresponding binary row for the cut-set matrix
    row = [0] * len(sorted_edges)
    for edge in cutset_edges:
      normalized_edge = tuple(sorted(edge))
      if normalized_edge in edge_to_index:
        row[edge_to_index[normalized_edge]] = 1
    matrix.append(row)

  return cutsets, matrix, sorted_edges