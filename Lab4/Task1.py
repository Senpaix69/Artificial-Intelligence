from queue import Queue

def path_cost(path):
    sum = 0
    for node in path:
        for pare in graph[node]:
            if pare['child'] in path:
                sum += pare['cost']
    return sum

def bfs(graph, start, goal):
    visited = set()
    queue = Queue()
    queue.put(start)
    parent = {}
    parent[start] = None
    
    while not queue.empty():
        node = queue.get()
        if node == goal:
            path = []
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return path, path_cost(path)
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor['child'] not in visited:
                queue.put(neighbor['child'])
                parent[neighbor['child']] = node
    
    return None

graph = {
    'S':[   {'child': 'A', 'cost': 3},
            {'child': 'D', 'cost': 2},
            {'child': 'C', 'cost': 2}
        ],
    'A': [],
    'D':[
            {'child': 'G','cost': 8},
            {'child': 'B','cost': 3}
        ],
    'C':[
            {'child': 'F','cost': 1}
        ],
    'B':[
            {'child': 'E','cost': 2}
        ],
    'F': [
            {'child': 'E','cost': 0},
            {'child': 'G','cost': 4}
        ],
    'E': [
            {'child': 'G','cost': 2}
        ],
    'G': [],
}

start = 'S'
goal = 'G'

path, cost = bfs(graph, start, goal)

if path is not None:
    print('The shortest path from', start, 'to', goal, 'is:', ' -> '.join(path))
    print("Minimum Cost: ", cost)
else:
    print('There is no path from', start, 'to', goal)