import queue as q
Graph = {
    'S': {'A':(1, 3),'G':(10, 0)},
    'A': {'B':(2, 4),'C':(1, 2)},
    'B': {'D':(5, 6)},
    'C': {'D':(3, 6),'G':(4, 0)},
    'D': {'G':(6, 0)},
    'G': {}
}
startingHeuristic = 5


def A_STR(MyGraph1, end, start):
    QU = q.PriorityQueue()
    value = startingHeuristic
    w = (0, (value, start))
    path = []
    QU.put(w)
    while QU:
        vertex = QU.get(0)
        print(vertex[0])
        n = vertex[-1][-1]
        if n not in path:
            path.append(n)
            if n == end:
                s = str(vertex)
                return path
                #return[s, vertex[0]]
            edges = list(MyGraph1[n].keys())
            print(edges)
            for i in range(len(edges)):
                add = list(vertex)
                add.append(edges[i])
                cost = vertex[0] + MyGraph1[n][edges[i]][0] + MyGraph1[n][edges[i]][1]
                t = (cost, add)
                QU.put(t)
                print(t)



cost = 0
path = []

#for i in range(0, len(arr)-1):
abc = A_STR(Graph, 'G', 'S')
 #   print("Path from ", arr[i], "to ", arr[i+1],  abc[0])
 #   print("cost: ", abc[1])
 #   path = path + list(abc[0])
 #   cost = cost + int(abc[1])