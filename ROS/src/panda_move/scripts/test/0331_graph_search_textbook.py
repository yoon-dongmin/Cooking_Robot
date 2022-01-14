from collections import deque
# AI modern approach
# https://github.com/aimacode/aima-python/blob/master/search.py#L15
# ==================================
# GraphProblem (from AI textbook)
# ==================================
# class Arc(object):
#     """An arc has a from_node and a to_node node and a (non-negative) cost"""
#     def __init__(self, from_node, to_node, cost=1, action=None):
#         assert cost >= 0, ("Cost cannot be negative for"+
#                            str(from_node)+"->"+str(to_node)+", cost: "+str(cost))
#         self.from_node = from_node
#         self.to_node = to_node
#         self.action = action
#         self.cost=cost

#     def __repr__(self):
#         """string representation of an arc"""
#         if self.action:
#             return str(self.from_node)+" --"+str(self.action)+"--> "+str(self.to_node)
#         else:
#             return str(self.from_node)+" --> "+str(self.to_node)

# class Search_problem(object):
#     """A search problem consists of:
#     * a start node
#     * a neighbors function that gives the neighbors of a node
#     * a specification of a goal
#     * a (optional) heuristic function.
#     The methods must be overridden to define a search problem."""

#     def start_node(self):
#         """returns start node"""
#         raise NotImplementedError("start_node")   # abstract method
    
#     def is_goal(self,node):
#         """is True if node is a goal"""
#         raise NotImplementedError("is_goal")   # abstract method

#     def neighbors(self,node):
#         """returns a list of the arcs for the neighbors of node"""
#         raise NotImplementedError("neighbors")   # abstract method

#     def heuristic(self,n):
#         """Gives the heuristic value of node n.
#         Returns 0 if not overridden."""
#         return 0

# class Search_problem_from_explicit_graph(Search_problem):
#     """A search problem consists of:
#     * a list or set of nodes
#     * a list or set of arcs
#     * a start node
#     * a list or set of goal nodes
#     * a dictionary that maps each node into its heuristic value.
#     * a dictionary that maps each node into its (x,y) position
#     """

#     def __init__(self, nodes, arcs, start=None, goals=set(), hmap={}, positions={}):
#         self.neighs = {}
#         self.nodes = nodes
#         for node in nodes:
#             self.neighs[node]=[]
#         self.arcs = arcs
#         for arc in arcs:
#             self.neighs[arc.from_node].append(arc)
#         self.start = start
#         self.goals = goals
#         self.hmap = hmap
#         self.positions = positions

#     def start_node(self):
#         """returns start node"""
#         return self.start
    
#     def is_goal(self,node):
#         """is True if node is a goal"""
#         return node in self.goals

#     def neighbors(self,node):
#         """returns the neighbors of node"""
#         return self.neighs[node]

#     def heuristic(self,node):
#         """Gives the heuristic value of node n.
#         Returns 0 if not overridden in the hmap."""
#         if node in self.hmap:
#             return self.hmap[node]
#         else:
#             return 0
        
#     def __repr__(self):
#         """returns a string representation of the search problem"""
#         res=""
#         for arc in self.arcs:
#             res += str(arc)+".  "
#         return res

#     def neighbor_nodes(self,node):
#         """returns an iterator over the neighbors of node"""
#         return (path.to_node for path in self.neighs[node])

# problem1 = Search_problem_from_explicit_graph(
#     {'s', 'a','b','c','d','g'},
#     [Arc('s','a',2), Arc('s','b',3), Arc('s','d',5), 
#     Arc('a','c',4), Arc('b','d',4), Arc('c','d',1),
#     Arc('c','g',2), Arc('d','g',5)],
#     start = 's',
#     goals = {'g'},
#     hmap={'s': 0, 'a': 2, 'b': 5, 'c': 2, 'd': 1, 'g': 0})

# ==================================
# Graph (from aipython)
# ==================================
class Graph:
    """A graph connects nodes (vertices) by edges (links). Each edge can also
    have a length associated with it. The constructor call is something like:
        g = Graph({'A': {'B': 1, 'C': 2})
    this makes a graph with 3 nodes, A, B, and C, with an edge of length 1 from
    A to B,  and an edge of length 2 from A to C. You can also do:
        g = Graph({'A': {'B': 1, 'C': 2}, directed=False)
    This makes an undirected graph, so inverse links are also added. The graph
    stays undirected; if you add more links with g.connect('B', 'C', 3), then
    inverse link is also added. You can use g.nodes() to get a list of nodes,
    g.get('A') to get a dict of links out of A, and g.get('A', 'B') to get the
    length of the link from A to B. 'Lengths' can actually be any object at
    all, and nodes can be any hashable object."""

    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):
        """Make a digraph into an undirected graph by adding symmetric edges."""
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.connect1(b, a, dist)

    def connect(self, A, B, distance=1):
        """Add a link from A and B of given distance, and also add the inverse
        link if the graph is undirected."""
        self.connect1(A, B, distance)
        if not self.directed:
            self.connect1(B, A, distance)

    def connect1(self, A, B, distance):
        """Add a link from A to B of given distance, in one direction only."""
        self.graph_dict.setdefault(A, {})[B] = distance

    def get(self, a, b=None):
        """Return a link distance or a dict of {node: distance} entries.
        .get(a,b) returns the distance or None;
        .get(a) returns a dict of {node: distance} entries, possibly {}."""
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    def nodes(self):
        """Return a list of nodes in the graph."""
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)

def UndirectedGraph(graph_dict=None):
    """Build a Graph where every edge (including future ones) goes both ways."""
    return Graph(graph_dict=graph_dict, directed=False)

""" [Figure 3.2]
Simplified road map of Romania
"""
romania_map = UndirectedGraph(dict(
    Arad=dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest=dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova=dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta=dict(Mehadia=75),
    Eforie=dict(Hirsova=86),
    Fagaras=dict(Sibiu=99),
    Hirsova=dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea=dict(Zerind=71, Sibiu=151),
    Pitesti=dict(Rimnicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=142)))
romania_map.locations = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531))

# ==================================
# Problem & Node
# ==================================
class Problem:
    def __init__(self, initial, goal=None):
        self.initial = initial
        self.goal = goal
    
    def is_goal(self, state):
        if self.goal == state:
            return True
        else:
            return False
    
    # def actions(self, state):
    #     raise NotImplementedError
    
    # def result(self, state, action):
    #     raise NotImplementedError
    
    # def goal_test(self, state):
    #     if isinstance(self.goal, list):
    #         return is_in(state, self.goal)
    #     else:
    #         return state == self.goal
    
    # def path_cost(self, c, state1, action, state2):
    #     return c + 1

    # def value(self, state):
    #     raise NotImplementedError

class GraphProblem(Problem):
    """The problem of searching a graph from one node to another."""

    def __init__(self, initial, goal, graph):
        super().__init__(initial, goal)
        self.graph = graph

    def actions(self, A):
        """The actions at a graph node are just its neighbors."""
        return list(self.graph.get(A).keys())

    def result(self, state, action):
        """The result of going to a neighbor is just that neighbor."""
        return action

    def path_cost(self, cost_so_far, A, action, B):
        return cost_so_far + (self.graph.get(A, B) or np.inf)

    # def find_min_edge(self):
    #     """Find minimum value of edges."""
    #     m = np.inf
    #     for d in self.graph.graph_dict.values():
    #         local_min = min(d.values())
    #         m = min(m, local_min)

    #     return m

    # def h(self, node):
    #     """h function is straight-line distance from a node's state to goal."""
    #     locs = getattr(self.graph, 'locations', None)
    #     if locs:
    #         if type(node) is str:
    #             return int(distance(locs[node], locs[self.goal]))

    #         return int(distance(locs[node.state], locs[self.goal]))
    #     else:
    #         return np.inf

class Node:
    def __init__(self, state, parent=None, action=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
    
    def child_node(self, problem, action):
        # problem.result(state, action) : state에서 action을 했을때 다음 state
        # problem.path_cost() : 현재 state까지의 path_cost에 (A->B)의 cost 더함
        next_state = problem.result(self.state, action)
        next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state))
        return next_node

    def expand(self, problem):
        children = []
        # problem.actions : state 에서 할 수 있는 action list return
        # child_node(problem, action) : 현재 node에서 action을 할때 가능한 다음 노드
        for action in problem.actions(self.state):
            children.append(self.child_node(problem, action))
        return children

# ==================================
# Search
# ==================================
def breadth_first_graph_search(problem):
    '''
    [Figure 3.11]
    '''
    # is_goal()
    # expand()
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node
    
    frontier = deque([node])
    explored_set = set()

    while frontier:
        node = frontier.popleft() # FIFO - 큐
        explored_set.add(node) # frontier에 들어가면 해줘야 되는것?
        for child in node.expand(problem):
            if (child.state not in explored_set) and (child.state not in frontier):
                print("child: ", child.state)
                if problem.is_goal(child.state):
                    return child
                frontier.append(child)
    return None

def depth_first_graph_search(problem):
    node = Node(problem.initial)
    if problem.is_goal(node.state):
        return node
    
    frontier = deque([node])
    explored_set = set()

    while frontier:
        node = frontier.pop() # LIFO - 스택
        explored_set.add(node) # frontier에 들어가면 해줘야 되는것?
        for child in node.expand(problem):
            if (child.state not in explored_set) and (child.state not in frontier):
                print("child: ", child.state)
                if problem.is_goal(child.state):
                    return child
                frontier.append(child)
    return None

def main():
    global romania_map
    problem1 = GraphProblem('Arad', 'Bucharest', romania_map)
    breadth_first_graph_search(problem1)
    # depth_first_graph_search(problem1)

if __name__ == '__main__':
    main()