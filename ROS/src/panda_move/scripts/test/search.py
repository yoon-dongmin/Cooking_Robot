class Search_problem(object):
    """A search problem consists of:
    * a start node
    * a neighbors function that gives the neighbors of a node
    * a specification of a goal
    * a (optional) heuristic function.
    The methods must be overridden to define a search problem."""

    def start_node(self):
        """returns start node"""
        raise NotImplementedError("start_node")   # abstract method
    
    def is_goal(self,node):
        """is True if node is a goal"""
        raise NotImplementedError("is_goal")   # abstract method

    def neighbors(self,node):
        """returns a list of the arcs for the neighbors of node"""
        raise NotImplementedError("neighbors")   # abstract method

    def heuristic(self,n):
        """Gives the heuristic value of node n.
        Returns 0 if not overridden."""
        return 0

class Arc(object):
    """An arc has a from_node and a to_node node and a (non-negative) cost"""
    def __init__(self, from_node, to_node, cost=1, action=None):
        assert cost >= 0, ("Cost cannot be negative for"+
                           str(from_node)+"->"+str(to_node)+", cost: "+str(cost))
        self.from_node = from_node
        self.to_node = to_node
        self.action = action
        self.cost=cost

    def __repr__(self):
        """string representation of an arc"""
        if self.action:
            return str(self.from_node)+" --"+str(self.action)+"--> "+str(self.to_node)
        else:
            return str(self.from_node)+" --> "+str(self.to_node)

class Search_problem_from_explicit_graph(Search_problem):
    """A search problem consists of:
    * a list or set of nodes
    * a list or set of arcs
    * a start node
    * a list or set of goal nodes
    * a dictionary that maps each node into its heuristic value.
    * a dictionary that maps each node into its (x,y) position
    """

    def __init__(self, nodes, arcs, start=None, goals=set(), hmap={}, positions={}):
        self.neighs = {}
        self.nodes = nodes
        for node in nodes:
            self.neighs[node]=[]
        self.arcs = arcs
        for arc in arcs:
            self.neighs[arc.from_node].append(arc)
        self.start = start
        self.goals = goals
        self.hmap = hmap
        self.positions = positions

    def start_node(self):
        """returns start node"""
        return self.start
    
    def is_goal(self,node):
        """is True if node is a goal"""
        return node in self.goals

    def neighbors(self,node):
        """returns the neighbors of node"""
        return self.neighs[node]

    def heuristic(self,node):
        """Gives the heuristic value of node n.
        Returns 0 if not overridden in the hmap."""
        if node in self.hmap:
            return self.hmap[node]
        else:
            return 0
        
    def __repr__(self):
        """returns a string representation of the search problem"""
        res=""
        for arc in self.arcs:
            res += str(arc)+".  "
        return res

    def neighbor_nodes(self,node):
        """returns an iterator over the neighbors of node"""
        return (path.to_node for path in self.neighs[node])

class Path(object):
    """A path is either a node or a path followed by an arc"""
    
    def __init__(self,initial,arc=None):
        """initial is either a node (in which case arc is None) or
        a path (in which case arc is an object of type Arc)"""
        self.initial = initial
        self.arc=arc
        if arc is None:
            self.cost=0
        else:
            self.cost = initial.cost+arc.cost

    def end(self):
        """returns the node at the end of the path"""
        if self.arc is None:
            return self.initial
        else:
            return self.arc.to_node

    def nodes(self):
        """enumerates the nodes for the path.
        This starts at the end and enumerates nodes in the path backwards."""
        current = self
        while current.arc is not None:
            yield current.arc.to_node
            current = current.initial
        yield current.initial

    def initial_nodes(self):
        """enumerates the nodes for the path before the end node.
        This starts at the end and enumerates nodes in the path backwards."""
        if self.arc is not None:
            for nd in self.initial.nodes(): yield nd     # could be "yield from"
        
    def __repr__(self):
        """returns a string representation of a path"""
        if self.arc is None:
            return str(self.initial)
        elif self.arc.action:
            return (str(self.initial)+"\n   --"+str(self.arc.action)
                    +"--> "+str(self.arc.to_node))
        else:
            return str(self.initial)+" --> "+str(self.arc.to_node)

problem1 = Search_problem_from_explicit_graph(
    {'a','b','c','d','g'},
    [Arc('a','c',1), Arc('a','b',3), Arc('c','d',3), Arc('c','b',1),
        Arc('b','d',1), Arc('b','g',3), Arc('d','g',1)],
    start = 'a',
    goals = {'g'},
    positions={'a': (0, 0), 'b': (1, 1), 'c': (0,1), 'd': (1,2), 'g': (2,2)})

# ==================================
# GraphProblem
# ==================================
graph = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}
class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state):
        pass

class Node:
    def __init__(self, state):
        self.state = state
        # self.parent
        # self.action
        # self.pat_cost
    
    def child_node(self, problem, action):
        
        pass

    def expand(self, problem):
        children = []
        for action in problem.actions(self.state):
            children.append(self.child_node(problem, action))
        return children

class GraphProblem(Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, state):
        """The actions at a graph node are just its neighbors."""
        return self.graph[state]

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        # return action

    def path_cost(self, cost_so_far, A, action, B):
        # return cost_so_far + (self.graph.get(A, B) or np.inf)

    def find_min_edge(self):
        """Find minimum value of edges."""
        # m = np.inf
        # for d in self.graph.graph_dict.values():
        #     local_min = min(d.values())
        #     m = min(m, local_min)

        # return m

    def h(self, node):
        """h function is straight-line distance from a node's state to goal."""
        # locs = getattr(self.graph, 'locations', None)
        # if locs:
        #     if type(node) is str:
        #         return int(distance(locs[node], locs[self.goal]))

        #     return int(distance(locs[node.state], locs[self.goal]))
        # else:
        #     return np.inf

# ==================================
# Uninformed Search
# ==================================
def breadth_first_graph_search(problem):
    '''
    [Figure 3.11]
    '''
    node = Node(problem.initial_state)
    if problem.is_goal(node.state):
        return node
    
    frontier = deque([node])
    expored_set = set()

    while frontier:
        node = frontier.popleft()
        explored_set.add(node) # frontier에 들어가면 해줘야 되는것?
        for child in node.expand(problem):
            if child.state not in explored_set and not in frontier:
                if problem.is_goal(child.state):
                    return child
                frontier.append(child)
    return None

# ==================================
# Informed Search
# ==================================
def a_star_search(problem):
    pass

def main():
    graph = # to-do
    initial = # to-do
    goal = # to-do
    test_problem = GraphProblem(initial, goal, graph)
    breadth_first_graph_search(test_problem)

if __name__ == '__main__':
    main()