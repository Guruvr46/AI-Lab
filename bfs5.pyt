from collections import deque

def bfs(graph, start):
    # Initialize a queue for BFS and add the start node to it
    queue = deque([start])
    
    # Initialize a set to keep track of visited nodes
    visited = set()
    
    # Mark the start node as visited
    visited.add(start)
    
    # Iterate while there are nodes in the queue
    while queue:
        # Pop the first node from the queue
        node = queue.popleft()
        print(node, end=" ")
        
        # Get all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Add the neighbor to the visited set and enqueue it
                visited.add(neighbor)
                queue.append(neighbor)

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Start BFS traversal from node 'A'
bfs(graph, 'A')
