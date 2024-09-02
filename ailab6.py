# DFS implementation in Python to search for the node with value 8 starting from node 4

# Function to perform DFS
def dfs(graph, start, target, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)

    print(f"Visiting node: {start}")

    if start == target:
        print(f"Target node {target} found!")
        return True

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, target, visited):
                return True

    return False

# Example graph represented as an adjacency list
graph = {
    1: [2, 3, 4],
    2: [5, 6],
    3: [],
    4: [7, 8],
    5: [9, 10],
    6: [],
    7: [11, 12],
    9: [],
    10: [],
    11: [],
    12: []
}

# Starting node
start_node = 4

# Target node to search for
target_node = 8

# Perform DFS
found = dfs(graph, start_node, target_node)

if not found:
    print(f"Target node {target_node} not found in the graph.")
