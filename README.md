# Graph Visualizer

Graph Visualizer is a Python application developed for the **Graph Theory** course at **Institut Teknologi Sepuluh Nopember (ITS)**.

The application allows the user to input either an **adjacency matrix** or an **incidence matrix** representing an undirected graph.

The program then:

1. Converts the input matrix into a graph.
2. Visualizes the graph.
3. Finds its fundamental cycles.
4. Generates the **Fundamental Cycle Matrix**.
5. Finds its fundamental cut-sets.
6. Generates the **Fundamental Cut-Set Matrix**.

---

## Team Members

-  Rida Bindech - 5999261011
-  Emmanuel Santini - 5999261124
-  Calixte Berthier - 5999261123

---

## Project Structure

```text
graph-visualizer/
│
├── main.py
├── input_parser.py
├── graph.py
├── vizualisation.py
├── fundamental_cycles.py
├── cutsets.py
└── README.md
```

### `main.py`

Main entry point of the application.

It connects all modules of the project:

```text
Input
  ↓
Matrix validation
  ↓
Graph creation
  ↓
Graph visualization
  ↓
Fundamental cycles
  ↓
Fundamental Cycle Matrix
  ↓
Fundamental cut-sets
  ↓
Fundamental Cut-Set Matrix
```

### `input_parser.py`

Handles user input and matrix validation.

The program accepts:

- Adjacency matrices
- Incidence matrices

For adjacency matrices, the program verifies that:

- The matrix is square.
- Values are either `0` or `1`.
- The diagonal contains only `0`.
- The matrix is symmetric.

For incidence matrices, the program verifies that:

- Values are either `0` or `1`.
- Every edge is incident to exactly two vertices.

### `graph.py`

Contains functions used to convert input matrices into a NetworkX graph.

It also provides:

- Graph information display.
- Deterministic edge ordering.
- A DFS-based spanning tree function.

A consistent edge order is important because the columns of the Fundamental Cycle Matrix and Fundamental Cut-Set Matrix must refer to the same edges.

### `vizualisation.py`

Contains functions used to:

- Draw the graph using NetworkX and Matplotlib.
- Display matrices in a readable format.

Edges are labelled:

```text
e1, e2, e3, ...
```

These labels correspond to the columns of the generated matrices.

### `fundamental_cycles.py`

Finds the fundamental cycles of the graph.

A spanning tree is first generated using Depth-First Search.

Every edge of the original graph that does not belong to the spanning tree is considered a **chord**.

Adding one chord to the spanning tree creates one fundamental cycle.

The module returns:

- The list of fundamental cycles.
- The Fundamental Cycle Matrix.
- The ordered list of graph edges.

### `cutsets.py`

Finds the fundamental cut-sets of the graph.

For every edge of the spanning tree:

1. The tree edge is temporarily removed.
2. The tree is separated into two connected components.
3. Every edge of the original graph connecting these two components is added to the cut-set.

The module returns:

- The list of fundamental cut-sets.
- The Fundamental Cut-Set Matrix.
- The ordered list of graph edges.

---

## Requirements

The project requires **Python 3** and the following libraries:

- NetworkX
- Matplotlib

Install the dependencies using:

```bash
pip install networkx matplotlib
```

or:

```bash
python -m pip install networkx matplotlib
```

---

## How to Run

Open a terminal inside the project directory and run:

```bash
python main.py
```

The program will ask which type of matrix you want to enter:

```text
==============================
        GRAPH VISUALIZER
==============================

Choose the input matrix type:
1 - Adjacency Matrix
2 - Incidence Matrix

Choice:
```

Enter:

```text
1
```

for an adjacency matrix, or:

```text
2
```

for an incidence matrix.

The matrix must be entered row by row, with values separated by spaces.

Press **ENTER on an empty line** when the matrix is complete.

---

# Sample Input / Output

## Example 1 — Adjacency Matrix

Consider a triangle graph containing three vertices.

Its adjacency matrix is:

```text
0 1 1
1 0 1
1 1 0
```

Example input:

```text
==============================
        GRAPH VISUALIZER
==============================

Choose the input matrix type:
1 - Adjacency Matrix
2 - Incidence Matrix

Choice: 1

Enter the matrix row by row.
Separate values with spaces.
Press ENTER on an empty line when finished.

0 1 1
1 0 1
1 1 0
```

After pressing ENTER on an empty line, the program creates the graph.

Example output:

```text
Graph successfully created.

Vertices:
[0, 1, 2]

Edges:
e1: 0 - 1
e2: 0 - 2
e3: 1 - 2
```

The graph is also displayed in a Matplotlib window.

---

## Fundamental Cycles

A DFS spanning tree is generated from the graph.

For the triangle graph, two edges belong to the spanning tree and the remaining edge is a chord.

Adding this chord creates one fundamental cycle.

Example:

```text
=== Fundamental Cycles ===

C1: [(0, 1), (1, 2), (0, 2)]
```

The corresponding Fundamental Cycle Matrix is:

```text
=== Fundamental Cycle Matrix ===

        e1      e2      e3
C1      1       1       1
```

A value of `1` means that the corresponding edge belongs to the fundamental cycle.

---

## Fundamental Cut-Sets

For every spanning-tree edge, the program temporarily removes the edge.

This divides the spanning tree into two components.

The program then identifies every edge of the original graph that connects these two components.

Example:

```text
=== Fundamental Cut-Sets ===

Q1: [(0, 1), (0, 2)]
Q2: [(1, 2), (0, 2)]
```

The corresponding matrix is:

```text
=== Fundamental Cut-Set Matrix ===

        e1      e2      e3
Q1      1       1       0
Q2      0       1       1
```

A value of `1` means that the corresponding edge belongs to the fundamental cut-set.

---

## Example 2 — Incidence Matrix

The same triangle graph can also be represented using an incidence matrix:

```text
1 1 0
1 0 1
0 1 1
```

Example input:

```text
Choice: 2

1 1 0
1 0 1
0 1 1
```

The program converts this matrix into the same graph:

```text
Vertices:
[0, 1, 2]

Edges:
e1: 0 - 1
e2: 0 - 2
e3: 1 - 2
```

The fundamental cycles and fundamental cut-sets are then calculated using the same process.

---

## Edge Ordering

The application uses a deterministic ordering for graph edges.

For example:

```text
e1 = (0, 1)
e2 = (0, 2)
e3 = (1, 2)
```

This same ordering is used for:

- Graph visualization.
- Fundamental Cycle Matrix columns.
- Fundamental Cut-Set Matrix columns.

This ensures that the generated matrices can be interpreted consistently.

---

## Technologies

- Python 3
- NetworkX
- Matplotlib

---

## AI Usage Disclosure

AI tools were used as assistance during the development of this project, mainly for:

- Code structure suggestions.
- Documentation.
- Debugging assistance.
- Explanation of graph theory concepts.

The prompt history used during development is provided separately with the homework submission.

All AI-generated suggestions were reviewed and adapted by the group members before being included in the final project.