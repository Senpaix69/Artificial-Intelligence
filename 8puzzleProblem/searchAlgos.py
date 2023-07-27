from time import time
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


class State:
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    greedy_evaluation = None
    AStar_evaluation = None
    heuristic = None

    def __init__(self, state, parent, direction, depth, cost):
        self.state = state
        self.parent = parent
        self.direction = direction
        self.depth = depth
        if parent:
            self.cost = parent.cost + cost
        else:
            self.cost = cost

    def test(self):  # check if the given state is goal
        return self.state == self.goal

    def Manhattan_Distance(self, n):  # heuristic function based on Manhattan distance
        self.heuristic = 0
        for i in range(1, n*n):
            distance = abs(self.state.index(i) - self.goal.index(i))
            # manhattan distance between the current state and goal state
            self.heuristic = self.heuristic + distance/n + distance % n

        self.greedy_evaluation = self.heuristic
        self.AStar_evaluation = self.heuristic + self.cost
        return (self.greedy_evaluation, self.AStar_evaluation)

    def Misplaced_Tiles(self, n):  # heuristic function based on number of misplaced tiles
        counter = 0
        self.heuristic = 0
        for i in range(n*n):
            for j in range(n*n):
                if (self.state[i] != self.goal[j]):
                    counter += 1
                self.heuristic = self.heuristic + counter

        self.greedy_evaluation = self.heuristic
        self.AStar_evaluation = self.heuristic + self.cost
        return (self.greedy_evaluation, self.AStar_evaluation)

    # this would remove illegal moves for a given state
    def available_moves(x, n):
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n * n - 1:
            moves.remove('Down')

        return moves

    # produces children of a given state
    def expand(self, n):
        x = self.state.index(0)
        # moves = self.available_moves(x,n)
        moves = ['Left', 'Right', 'Up', 'Down']
        if x % n == 0:
            moves.remove('Left')
        if x % n == n-1:
            moves.remove('Right')
        if x - n < 0:
            moves.remove('Up')
        if x + n > n*n - 1:
            moves.remove('Down')

        children = []
        for direction in moves:
            temp = self.state.copy()
            if direction == 'Left':
                temp[x], temp[x - 1] = temp[x - 1], temp[x]
            elif direction == 'Right':
                temp[x], temp[x + 1] = temp[x + 1], temp[x]
            elif direction == 'Up':
                temp[x], temp[x - n] = temp[x - n], temp[x]
            elif direction == 'Down':
                temp[x], temp[x + n] = temp[x + n], temp[x]

            # depth should be changed as children are produced
            children.append(State(temp, self, direction, self.depth + 1, 1))
        return children

    # gets the given state and returns it's direction + it's parent's direction till there is no parent
    def solution(self):
        solution = []
        solution.append(self.direction)
        path = self
        while path.parent != None:
            path = path.parent
            solution.append(path.direction)
        solution = solution[:-1]
        solution.reverse()
        return solution


def BFS(given_state, n):
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = Queue()
    frontier.put(root)
    explored = []
    while not (frontier.empty()):
        current_node = frontier.get()
        explored.append(current_node.state)
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return


def DFS(given_state, n):  # Depth-first Search with limited depth
    root = State(given_state, None, None, 0, 0)
    if root.test():
        return root.solution()
    frontier = LifoQueue()
    frontier.put(root)
    explored = []
    while not (frontier.empty()):
        current_node = frontier.get()
        max_depth = current_node.depth  # current depth
        explored.append(current_node.state)
        if max_depth == 30:
            continue  # go to the next branch
        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                if child.test():
                    return child.solution(), len(explored)
                frontier.put(child)
    return (("Couldn't find solution in the limited depth."), len(explored))


def Greedy(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # root.evaluation()
    # we can use Misplaced_Tiles() instead.
    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation[0], counter, root))  # based on greedy evaluation

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                # we can use Misplaced_Tiles() instead.
                evaluation = child.Manhattan_Distance(n)
                # based on greedy evaluation
                frontier.put((evaluation[0], counter, child))
    return


def AStar_search(given_state, n):
    frontier = PriorityQueue()
    explored = []
    counter = 0
    root = State(given_state, None, None, 0, 0)
    # root.evaluation()
    # we can use Misplaced_Tiles() instead.
    evaluation = root.Manhattan_Distance(n)
    frontier.put((evaluation[1], counter, root))

    while not frontier.empty():
        current_node = frontier.get()
        current_node = current_node[2]
        explored.append(current_node.state)

        if current_node.test():
            return current_node.solution(), len(explored)

        children = current_node.expand(n)
        for child in children:
            if child.state not in explored:
                counter += 1
                # we can use Misplaced_Tiles() instead.
                evaluation = child.Manhattan_Distance(n)
                # based on greedy evaluation
                frontier.put((evaluation[1], counter, child))
    return


n = 3
print("Enter your", n, "*", n, "puzzle")
# 1,8,2,0,4,3,7,6,5 is solvable
# 2,1,3,4,5,6,7,8,0 is not solvable
root = [1, 2, 3, 6, 7, 8, 4, 5, 0]
# for i in range(0,n*n):
#    p = int(input())
#    root.append(p)

print("The given state is:", root)


def inv_num(puzzle):  # count the number of inversions
    inv = 0
    for i in range(len(puzzle)-1):
        for j in range(i+1, len(puzzle)):
            if ((puzzle[i] > puzzle[j]) and puzzle[i] and puzzle[j]):
                inv += 1
    return inv


# check if initial state puzzle is solvable: number of inversions should be even.
def solvable(puzzle):
    inv_counter = inv_num(puzzle)
    if (inv_counter % 2 == 0):
        return True
    return False


if solvable(root):
    print("Solvable, please wait. \n")
    time1 = time()
    BFS_solution = BFS(root, n)
    BFS_time = time() - time1
    print('BFS Solution is ', BFS_solution[0])
    print('Number of explored nodes is ', BFS_solution[1])
    print('BFS Time:', BFS_time, "\n")
    # time2 = time()
    # DFS_solution = DFS(root, n)
    # DFS_time = time() - time2
    # print('DFS Solution is ', DFS_solution[0])
    # print('Number of explored nodes is ', DFS_solution[1])
    # print('DFS Time:', DFS_time, "\n")

    time3 = time()
    Greedy_solution = Greedy(root, n)
    Greedy_time = time() - time3
    print('Greedy Solution is ', Greedy_solution[0])
    print('Number of explored nodes is ', Greedy_solution[1])
    print('Greedy Time:', Greedy_time, "\n")

    time4 = time()
    AStar_solution = AStar_search(root, n)
    AStar_time = time() - time4
    print('A* Solution is ', AStar_solution[0])
    print('Number of explored nodes is ', AStar_solution[1])
    print('A* Time:', AStar_time)

else:
    print("Not solvable")
