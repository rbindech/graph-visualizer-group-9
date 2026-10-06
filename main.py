from input_parser import get_graph_input

from graph import (
    adjacency_to_graph,
    incidence_to_graph,
    get_ordered_edges,
    print_graph_info
)

from visualization import (
    draw_graph,
    print_matrix
)

from fundamental_cycles import get_fundamental_cycles
from cutsets import get_fundamental_cutsets


def main():
    try:
        # ==================================================
        # 1. GET MATRIX FROM USER
        # ==================================================

        matrix_type, matrix = get_graph_input()

        # ==================================================
        # 2. CONVERT MATRIX TO GRAPH
        # ==================================================

        if matrix_type == "adjacency":
            graph = adjacency_to_graph(matrix)
        else:
            graph = incidence_to_graph(matrix)

        print("\nGraph successfully created.")

        # Display vertices and ordered edges
        print_graph_info(graph)

        # ==================================================
        # 3. GET A CONSISTENT EDGE ORDER
        # ==================================================

        edges_order = get_ordered_edges(graph)

        edge_labels = []

        for i in range(len(edges_order)):
            edge_labels.append("e" + str(i + 1))

        # ==================================================
        # 4. VISUALIZE GRAPH
        # ==================================================

        draw_graph(
            graph,
            edges_order,
            title="Graph Visualization"
        )

        # ==================================================
        # 5. FUNDAMENTAL CYCLES
        # ==================================================

        cycles, cycle_matrix, cycle_edges_order = (
            get_fundamental_cycles(graph)
        )

        print("\n=== Fundamental Cycles ===")

        if len(cycles) == 0:
            print("No fundamental cycle found.")
        else:
            for i in range(len(cycles)):
                print(
                    "C" + str(i + 1) + ":",
                    cycles[i]
                )

        cycle_row_labels = []

        for i in range(len(cycle_matrix)):
            cycle_row_labels.append(
                "C" + str(i + 1)
            )

        print_matrix(
            cycle_matrix,
            cycle_row_labels,
            edge_labels,
            title="Fundamental Cycle Matrix"
        )

        # ==================================================
        # 6. FUNDAMENTAL CUT-SETS
        # ==================================================

        cutsets, cutset_matrix, cutset_edges_order = (
            get_fundamental_cutsets(graph)
        )

        print("\n=== Fundamental Cut-Sets ===")

        if len(cutsets) == 0:
            print("No fundamental cut-set found.")
        else:
            for i in range(len(cutsets)):
                print(
                    "Q" + str(i + 1) + ":",
                    cutsets[i]
                )

        cutset_row_labels = []

        for i in range(len(cutset_matrix)):
            cutset_row_labels.append(
                "Q" + str(i + 1)
            )

        print_matrix(
            cutset_matrix,
            cutset_row_labels,
            edge_labels,
            title="Fundamental Cut-Set Matrix"
        )

        # ==================================================
        # 7. FINISHED
        # ==================================================

        print("Graph analysis completed successfully.")


    except ValueError as error:
        print("\nInput error:", error)

    except Exception as error:
        print("\nUnexpected error:", error)


if __name__ == "__main__":
    main()