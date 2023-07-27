class Node:
    def __init__(self, parent, children, isleaf, value, MaxNode, MinNode, pcount):
        self.parent = parent 
        self.children = children
        self.isleaf = isleaf
        self.value = value
        self.MaxNode = MaxNode
        self.MinNode = MinNode
        self.pcount = pcount

Graph = {
    'S': Node(None, ['a', 'h'], False, None, True, False, 2),
    'a': Node('S', ['b','e'], False, None, False, True, 2),
    'h': Node('S', ['i','l'], False, None, False, True, 2),
    'b': Node('a', ['c','d'], False, None, True, False, 2),
    'e': Node('a', ['f','g'], False, None, True, False, 2),
    'i': Node('h', ['j','k'], False, None, True, False, 2),
    'l': Node('h', ['m','n'], False, None, True, False, 2),
    'c': Node('b', None, True, 10, False, True, None),
    'd': Node('b', None, True, 6, False, True, None),
    'f': Node('e', None, True, 100, False, True, None),
    'g': Node('e', None, True, 8, False, True, None),
    'j': Node('i', None, True, 1, False, True, None),
    'k': Node('i', None, True, 2, False, True, None),
    'm': Node('l', None, True, 20, False, True, None),
    'n': Node('l', None, True, 4, False, True, None),
}



def alphabeta(Node,alpha, beta):
    if (Graph[Node].isleaf):
        return Graph[Node].value
    
    elif (Graph[Node].MaxNode):
        for child in Graph[Node].children:
            Graph[Node].pcount -= 1
            alpha = max(alpha,alphabeta(child,alpha, beta))
            if alpha >= beta:
                return beta
            
        return alpha
        
    elif (Graph[Node].MinNode):
        for child in Graph[Node].children:
            Graph[Node].pcount -= 1
            beta = min(beta,alphabeta(child,alpha, beta))
            if alpha >= beta:
                return alpha
            
        return beta

if __name__ == "__main__":
    import math
    print(alphabeta('S', -math.inf, math.inf))
    prunnedlist = [key for key in Graph.keys() if Graph[key].pcount is not None and Graph[key].pcount > 0]
    print (prunnedlist)
