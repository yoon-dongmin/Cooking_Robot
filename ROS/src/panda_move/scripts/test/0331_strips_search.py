# STRIPS
# http://aipython.org

# ==================================
# STRIPS
# ==================================
class Strips:
    def __init__(self, name, preconds, effects, cost=1):
        """
        defines the STRIPS representation for an action:
        * name is the name of the action
        * preconds, the preconditions, is feature:value dictionary that must hold
        for the action to be carried out
        * effects is a feature:value map that this action makes
        true. The action changes the value of any feature specified
        here, and leaves other features unchanged.
        * cost is the cost of the action
        """
        self.name = name
        self.preconds = preconds
        self.effects = effects
        self.cost = cost

    def __repr__(self):
        return self.name

class StripsDomain:
    def __init__(self, feats_vals, actions):
        """Problem domain
        feats_vals is a feature:domain dictionary, 
                mapping each feature to its domain
        actions
        """
        self.feats_vals = feats_vals
        self.actions = actions

# ==================================
# Problem
# ==================================
class PlanningProblem:
    def __init__(self, prob_domain, initial_state, goal):
        """
        a planning problem consists of
        * a planning domain
        * the initial state
        * a goal 
        """
        self.prob_domain = prob_domain
        self.initial_state = initial_state
        self.goal = goal

# ==================================
# Blocks World
# ==================================
def move(x,y,z):
    """string for the 'move' action"""
    return 'move_'+x+'_from_'+y+'_to_'+z
def on(x):
    """string for the 'on' feature"""
    return x+'_is_on'
def clear(x):
    """string for the 'clear' feature"""
    return 'clear_'+x
def create_blocks_world(blocks = {'a','b','c','d'}):
    boolean = {True, False}
    
    # stmap 
    # => action space
    # => set(len of 18) : 가능한 모든 action을 정의 (cost, effects, preconds)
    blocks_and_table = blocks | {'table'}
    stmap =  {Strips(move(x,y,z),{on(x):y, clear(x):True, clear(z):True}, 
                                 {on(x):z, clear(y):True, clear(z):False})
                    for x in blocks
                    for y in blocks_and_table
                    for z in blocks
                    if x!=y and y!=z and z!=x}
    stmap.update({Strips(move(x,y,'table'), {on(x):y, clear(x):True}, 
                                 {on(x):'table', clear(y):True})
                    for x in blocks
                    for y in blocks
                    if x!=y})
    # print("="*50)
    # print("action space = stmap", type(stmap))
    # print("="*50)
    # for item in stmap:
    #     print("action: ", item)
    #     print("precond=", item.preconds)
    #     print("effect=", item.effects)
    #     print("cost=", item.cost)
    #     print()
    print(stmap)
    exit()

    # feats_vals
    # => state space
    # => dict(len of 7)
    feats_vals = {on(x):blocks_and_table-{x} for x in blocks}
    feats_vals.update({clear(x):boolean for x in blocks_and_table})
    # print("="*50)
    # print("state space = feats_vals", type(feats_vals))
    # print("="*50)
    # for item in feats_vals:
    #     print(item, type(item))

    return StripsDomain(feats_vals, stmap)

blocks1dom = create_blocks_world({'a','b','c'})
initial1 = {on('a'):'table', clear('a'):True,
                on('b'):'c',  clear('b'):True,
                on('c'):'table', clear('c'):False}
goal1 = {on('a'):'b', on('c'):'a'}
blocks1 = PlanningProblem(blocks1dom, initial1, goal1)

# ==================================
# Searcher
# ==================================
# SearcherMPP + AStarSearcher + Searcher (v)
# Class Arc
# Class Path
import heapq

class Path:
    def __init__(self, initial, arc=None):
        self.initial = initial
        self.arc = arc 
        if arc is None:
            self.cost = 0
        else:
            self.cost = initial.cost + arc.cost


    def end(self):
        """ path의 마지막 node를 반환 """
        if self.arc is None:
            return self.initial
        else:
            return self.arc.to_node

    def nodes(self):
        """ path를 위해서 node를 enumerate
        끝에서부터 시작해서 path에 있는 node를 거꾸로 enumerate """
        current = self
        while current.arc is not None:
            yield current.arc.to_node
            current = current.initial
        yield current.initial

    def initial_node(self):
        if self.arc is not None:
            for nd in self.initial.node(): yield nd

    def __repr__(self):
        if self.arc is None:
            return str(self.initial)
        elif self.arc.action:
            return (str(self.initial)+"\n   --"+str(self.arc.action)
                    +"--> "+str(self.arc.to_node))
        else:
            return str(self.initial)+" --> "+str(self.arc.to_node)

class FrontierPQ:
    def __init__(self):
        self.frontier_index = 0 # 이제껏 frontier에 add된 item수
        self.frontierpq = []

    def empty(self):
        """ priority queue가 empty면 True를 반환 """
        return self.frontierpq == []

    def add(self, path, value):
        """ priority queue에 path를 add, value를 기준으로 sort """
        self.frontier_index += 1
        heapq.heappush(self.frontierpq, (value, -self.frontier_index, path)) ## 왜 -를 붙여서 add?

    def pop(self):
        """ 최소의 value를 가지는 frontier의 path를 제거하여 반환 """
        (_, _, path) = heapq.heappop(self.frontierpq)
        return path

    def count(self, val):
        """ frontier에 있는 element 중 val과 동일한 value를 가지는 수를 반환 """
        return sum(1 for e in self.frontierpq if e[0] == val)

    def __repr__(self):
        NotImplementedError

    def __len__(self):
        NotImplementedError

    def __iter__(self):
        NotImplementedError

class AStarSearcher:
    def __init__(self, problem):
        self.problem = problem
        self.num_expanded = 0
        self.initialize_frontier() # 문제가 있을수 있음
        self.add_to_frontier(Path(problem.start_node()))
        self.explored = set()

    def search(self):
        """ goal에 도달하면 path return 아니면 None을 return """
        while not self.empty_frontier():
            path = self.frontier.pop()
            self.num_expanded += 1
            if self.problem.is_goal(path.end()):
                self.solution = path
                return path
            else:
                neighs = self.problem.neighbors(path.end())
                for arc in neighs:
                    self.add_to_frontier(Path(path, arc))

    def initialize_frontier(self):
        self.frontier = FrontierPQ()

    def empty_frontier(self):
        return self.frontier.empty()

    def add_to_frontier(self, path):
        value = path.cost + self.problem.heuristic(path.end())
        self.frontier.add(path, value)

# ==================================
# Planner
# ==================================
class Arc:
    def __init__(self, from_node, to_node, cost=1, action=None):
        assert cost >= 0, ("Cost cannot be negative for {}->{}, cost:{}").format(from_node, to_node, cost)
        self.from_node = from_node
        self.to_node = to_node
        self.action = action
        self.cost = cost

class State:
    def __init__(self, assignment):
        self.assignment = assignment
        self.hash_value = None
    def __hash__(self):
        """ comment """
        if self.hash_value is None:
            self.hash_value = hash(frozenset(self.assignment.items()))
        return self.hash_value
    def __eq__(self,st):
        return self.assignment == st.assignment
    def __str__(self):
        return str(self.assignment)

def zero(*args, **nargs):
    """ 항상 0을 return """
    return 0

# Search_problem + ForwardPlanning
class ForwardPlanning:
    def __init__(self, planning_problem, heur=zero):
        self.prob_domain = planning_problem.prob_domain
        self.initial_state = State(planning_problem.initial_state)
        self.goal = planning_problem.goal
        self.heur = heur
    
    def is_goal(self, state):
        """ 주어진 state가 goal이면 True를 반환 """
        return all(state.assignment[prop] == self.goal[prop] for prop in self.goal)

    def start_node(self):
        """ 주어진 start node를 반환 """
        return self.initial_state

    def neighbors(self, state):
        """ 주어진 state의 neighbor를 반환 """
        return [ Arc(state, self.effect(act, state.assignment), act.cost, act)
                for act in self.prob_domain.actions
                if self.possible(act, state.assignment)]

    def possible(self, act, state_asst):
        """ 주어진 state에서 act가 possible 하면 True를 반환 """
        return all(state_asst[pre] == act.preconds[pre] for pre in act.preconds)
        # act.possible(state_asst)

    def effect(self, act, state_asst):
        """ 주어진 state_asst에서 act를 하는 것의 effect(state)를 반환 
        state_asst에 effect의 asst을 추가하여 state생성 """
        new_state_asst = state_asst.copy()
        new_state_asst.update(act.effects)
        return State(new_state_asst)
        # act.effects(state_asst)

    def heuristic(self, state):
        """ heuristic은 state에서 goal까지 cost의 (under)estimate value """
        # self.heur(state.assignment, self.goal)
        return 0 ## 반드시 수정!!!!!!!!!!!!!!

class BackwardPlanning():
    def __init__(self):
        pass

# ==================================
# main
# ==================================
def main():
    global blocks1
    # path = AStarSearcher(ForwardPlanning(blocks1)).search()

    print("!")

if __name__ == '__main__':
    main()