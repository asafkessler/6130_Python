class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []


def max_path_dag_recursive(node):
    if not node.neighbors:
        return node.value

    max_sum = float('-inf')
    for neighbor in node.neighbors:
        max_sum = max(max_sum, node.value + max_path_dag_recursive(neighbor))

    return max_sum


# Example usage
if __name__ == "__main__":
    nodes = [Node(value) for value in [1, 2, 3, 4, 5, 6]]

    nodes[0].neighbors = [nodes[1], nodes[2]]
    nodes[1].neighbors = [nodes[3], nodes[4]]
    nodes[2].neighbors = [nodes[4], nodes[5]]
    nodes[3].neighbors = [nodes[4]]
    nodes[4].neighbors = [nodes[5]]

    start_node = nodes[0]
    max_path_sum = max_path_dag_recursive(start_node)
    print("Max Path Sum:", max_path_sum)