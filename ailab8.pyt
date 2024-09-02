from queue import PriorityQueue

# Define the Romania map as a dictionary
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101}
}

# Heuristic function (straight-line distance to Bucharest)
def h(node):
    heuristics = {
        'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242, 'Eforie': 161,
        'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 'Iasi': 226, 'Lugoj': 244,
        'Mehadia': 241, 'Neamt': 234, 'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
        'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 'Zerind': 374
    }
    return heuristics[node]

def best_first_search(start, goal):
    frontier = PriorityQueue()
    frontier.put((h(start), start))
    came_from = {}
    came_from[start] = None

    while not frontier.empty():
        _, current = frontier.get()

        if current == goal:
            break

        for next_node in romania_map[current]:
            if next_node not in came_from:
                priority = h(next_node)
                frontier.put((priority, next_node))
                came_from[next_node] = current

    return came_from

def reconstruct_path(came_from, start, goal):
    path = [goal]
    current = goal
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

start_city = 'Zerind'
goal_city = 'Bucharest'
came_from = best_first_search(start_city, goal_city)
path = reconstruct_path(came_from, start_city, goal_city)
print(f"Path from {start_city} to {goal_city}: {path}")
