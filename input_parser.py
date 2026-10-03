def read_matrix():
    """
    Ask the user to enter a matrix row by row.

    Example:
        0 1 1
        1 0 1
        1 1 0

    An empty line ends the input.
    """
    matrix = []

    print("\nEnter the matrix row by row.")
    print("Separate values with spaces.")
    print("Press ENTER on an empty line when finished.\n")

    while True:
        line = input()

        if line.strip() == "":
            break

        try:
            row = [int(value) for value in line.split()]
            matrix.append(row)
        except ValueError:
            raise ValueError("The matrix must contain integers only.")

    if not matrix:
        raise ValueError("The matrix cannot be empty.")

    return matrix


def validate_same_row_length(matrix):
    """
    Check that all rows contain the same number of elements.
    """
    expected_length = len(matrix[0])

    for row in matrix:
        if len(row) != expected_length:
            raise ValueError(
                "Invalid matrix: all rows must have the same length."
            )


def validate_adjacency_matrix(matrix):
    """
    Validate an adjacency matrix for a simple undirected graph.

    Conditions:
    - matrix must be square
    - values must be 0 or 1
    - diagonal must contain 0
    - matrix must be symmetric
    """

    validate_same_row_length(matrix)

    rows = len(matrix)
    columns = len(matrix[0])

    if rows != columns:
        raise ValueError(
            "Adjacency matrix must be square."
        )

    for i in range(rows):
        for j in range(columns):

            if matrix[i][j] not in (0, 1):
                raise ValueError(
                    "Adjacency matrix can only contain 0 and 1."
                )

            if i == j and matrix[i][j] != 0:
                raise ValueError(
                    "Diagonal values must be 0 for a simple graph."
                )

            if matrix[i][j] != matrix[j][i]:
                raise ValueError(
                    "Adjacency matrix must be symmetric "
                    "for an undirected graph."
                )

    return True


def validate_incidence_matrix(matrix):
    """
    Validate an incidence matrix for a simple undirected graph.

    For each edge/column:
    exactly two vertices must contain 1.
    """

    validate_same_row_length(matrix)

    rows = len(matrix)
    columns = len(matrix[0])

    for row in matrix:
        for value in row:
            if value not in (0, 1):
                raise ValueError(
                    "Incidence matrix can only contain 0 and 1."
                )

    for column in range(columns):

        number_of_incident_vertices = 0

        for row in range(rows):
            if matrix[row][column] == 1:
                number_of_incident_vertices += 1

        if number_of_incident_vertices != 2:
            raise ValueError(
                f"Invalid incidence matrix: edge {column + 1} "
                "must be connected to exactly two vertices."
            )

    return True


def get_graph_input():
    """
    Ask the user for the matrix type and matrix.

    Returns:
        matrix_type: "adjacency" or "incidence"
        matrix: list[list[int]]
    """

    print("==============================")
    print("        GRAPH VISUALIZER")
    print("==============================")

    print("\nChoose the input matrix type:")
    print("1 - Adjacency Matrix")
    print("2 - Incidence Matrix")

    choice = input("\nChoice: ").strip()

    if choice == "1":
        matrix_type = "adjacency"

    elif choice == "2":
        matrix_type = "incidence"

    else:
        raise ValueError(
            "Invalid choice. Please choose 1 or 2."
        )

    matrix = read_matrix()

    if matrix_type == "adjacency":
        validate_adjacency_matrix(matrix)

    else:
        validate_incidence_matrix(matrix)

    return matrix_type, matrix