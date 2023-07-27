from collections import deque

def DFS(graph, start):
    visit = set()
    stack = [start]
    tree = []
    while stack:
        node = stack.pop()
        if node not in visit:
            tree.append(node)
            visit.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visit)
    return tree

def BFS(graph, start):
    visit = set()
    queue = deque([start])
    tree = []
    while queue:
        node = queue.popleft()
        if node not in visit:
            tree.append(node)
            visit.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visit)
    return tree

def DFS_PATH(graph, start, end, path = []):
    path = path + [start]
    if start not in graph:
        return None
    if start == end:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = DFS_PATH(graph, neighbor, end, path)
            if new_path:
                return new_path
    return None
        
def BFS_PATH(graph, start, end):
    if start not in graph:
        return None
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        for neighbor in graph[node]:
            if neighbor not in path:
                queue.append((neighbor, path +[neighbor]))

def costcal(graph, path):
    total_cost = 0
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]   
        if current_node in graph and next_node in graph[current_node]:
            edge_cost = graph[current_node][next_node]
            total_cost += edge_cost
        else:
            return None   
    return total_cost

my_graph = {
    '1': {'2': 9, '4': 2},
    '2': {'1': 2, '4': 5},
    '3': {},
    '4': {'6': 4, '8': 2},
    '5': {'8': 1},
    '6': {},
    '7': {'5': 2, '3': 6, '6': 3},
    '8': {},
}

print("DFS Searched: ", DFS(my_graph, '1'))
print("DFS_PATH :", DFS_PATH(my_graph, '1', '8'))
print("Cost: ", costcal(my_graph, DFS_PATH(my_graph, '1', '8')))

print("\n")

print("BFS Searched: ", BFS(my_graph, '1'))
print("BFS_PATH :", BFS_PATH(my_graph, '1', '8'))
print("Cost: ", costcal(my_graph, BFS_PATH(my_graph, '1', '8')))