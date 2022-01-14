from collections import deque, defaultdict
import itertools
import heapq

REMOVED = '<removed-task>'

# ==================================
# Graph Problem
# ==================================
class GraphProblem:
    def __init__(self, initial, goal, graph_g, graph_h):
        self.initial = initial
        self.goal = goal
        self.g = graph_g
        self.h = graph_h
    
    def is_goal(self, state):
        if state in self.goal:
            return True
        else:
            return False

    def expand(self, state):
        return list(self.g[state].keys())

# ==================================
# Priority Queue
# ==================================
class PriorityQueue:
    def __init__(self):
        self.pq = []                         
        self.entry_finder = {}
        self.counter = itertools.count()
        self.g = defaultdict(int)
    
    def push(self, task, priority=0):
        if task in self.entry_finder:
            self.remove_task(task)
            
        count = next(self.counter)
        entry = [priority, count, task]
        
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
        
    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        while self.pq:
            [priority, count, task] = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return priority, task

class PriorityQueue1:
    def __init__(self):
        self.pq = []                         
        self.entry_finder = {}
        self.counter = itertools.count()
    
    def push(self, task, g=0, h=0):
        if task in self.entry_finder:
            self.remove_task(task)
            
        count = next(self.counter)
        entry = [h, count, g, task]
        
        self.entry_finder[task] = entry
        heapq.heappush(self.pq, entry)
        
    def remove_task(self, task):
        entry = self.entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop(self):
        while self.pq:
            [h, count, g, task] = heapq.heappop(self.pq)
            if task is not REMOVED:
                del self.entry_finder[task]
                return h, g, task

# ==================================
# Search
# ==================================
def bfs_test(problem):
    initial = problem.initial

    frontier = deque([initial])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node)
        for child in problem.expand(node):
            if (child not in frontier) and (child not in explored):
                # print('expanded: ', child)
                if problem.is_goal(child):
                    return child
                frontier.append(child)
    return None

def breadth_first_graph_search(problem):
    initial = problem.initial

    frontier_path = deque([initial])
    explored = set()
    # expanded = [initial]
    expanded = []

    while frontier_path:
        node_path = frontier_path.popleft()
        explored.add(node_path[-1])
        if node_path[-1] not in expanded:
            expanded.append(node_path[-1]) ##
        if problem.is_goal(node_path[-1]):
            return node_path, expanded
        for child in problem.expand(node_path[-1]):
            if child not in explored:
                # print(frontier_path)
                frontier_path.append(node_path+child)
    return None, None
    
def depth_first_graph_search(problem):
    initial = problem.initial

    frontier_path = [initial]
    explored = set()
    expanded = []

    while frontier_path:
        node_path = frontier_path.pop()
        explored.add(node_path[-1])
        expanded.append(node_path[-1])
        if problem.is_goal(node_path[-1]):
            return node_path, expanded
        for child in reversed(problem.expand(node_path[-1])):
            if child not in explored:
                # print(frontier_path)
                frontier_path.append(node_path+child)
        print(frontier_path)
    return None, None

def greedy_best_first_graph_search(problem):
    initial = problem.initial

    frontier = []
    heapq.heappush(frontier, (problem.h[initial], initial))
    explored = set()
    path = []

    while frontier:
        h, node = heapq.heappop(frontier)
        explored.add(node)
        path.append(node)
        for child in problem.expand(node):
            if (child not in frontier) and (child not in explored):
                if problem.is_goal(child):
                    path.append(child)
                    return path
                heapq.heappush(frontier, (problem.h[child], child))

def uniform_cost_search(problem):
    initial = problem.initial

    frontier = PriorityQueue()
    frontier.push(initial, 0)
    explored = set()

    expanded = []

    while frontier:
        g, node = frontier.pop()
        expanded.append(node)
        if problem.is_goal(node):
            return expanded
        explored.add(node)

        for child in problem.expand(node):
            if child not in explored:
                total_g = problem.g[node][child] + g
                # 만약에 frontier에 이미 있으면서, total_cost가 적으면 replace
                # frontier에 없으면 그냥 add
                if child in frontier.entry_finder:
                    if total_g < frontier.entry_finder[child][0]:
                        frontier.push(child, total_g)
                else:
                    frontier.push(child, total_g)

def astar_search(problem):
    initial = problem.initial

    frontier = PriorityQueue1()
    frontier.push(initial, 0, problem.h[initial])
    explored = set()

    expanded = []

    while frontier:
        h, g, node = frontier.pop()
        expanded.append(node)
        if problem.is_goal(node):
            return expanded
        explored.add(node)

        for child in problem.expand(node):
            if child not in explored:
                total_g = g + problem.g[node][child]
                total_h = total_g + problem.h[child]
                # 만약에 frontier에 이미 있으면서, total_cost가 적으면 replace
                # frontier에 없으면 그냥 add
                if child in frontier.entry_finder:
                    if total_h < frontier.entry_finder[child][0]:
                        frontier.push(child, total_g, total_h)
                else:
                    frontier.push(child, total_g, total_h)

def make_graph_problem_cs188():
    graph_g = {'s': {'A': 2, 'B': 3, 'D': 5},
            'A': {'s': 2, 'C': 4}, 
            'B': {'s': 3, 'D': 4},
            'C': {'A': 4, 'D': 1, 'g': 2}, 
            'D': {'s': 5, 'B': 4, 'C': 1, 'g': 5}, 
            'g': {'C': 2, 'D': 5}}
    graph_h = {'s': 100, 'A': 2, 'B': 5, 'C': 2, 'D': 1, 'g': 0}
    problem = GraphProblem('s', ['g'], graph_g, graph_h)
    return problem

def make_graph_problem_cs561():
    graph_g = {'S': {'A': 4, 'B': 3, 'C': 2},
            'A': {'S': 4, 'D': 1, 'E': 2}, 
            'B': {'S': 3, 'E': 2, 'F': 2},
            'C': {'S': 2, 'H': 1}, 
            'D': {'A': 1, 'I': 6},
            'E': {'A': 2, 'B': 2, 'J': 4}, 
            'F': {'B': 2, 'J': 2, 'g': 5},
            'H': {'C': 1},
            'I': {'D': 6, 'G': 2},
            'J': {'E': 4, 'F': 2, 'G': 3},
            'g': {'F': 5},
            'G': {'I': 2, 'J': 3}}
    graph_h = {'S': 9, 'A': 6, 'B': 7, 'C': 8, 'D': 4, 'E': 3, 
                'F': 6, 'H': 7, 'I': 3, 'J': 2, 'g': 0, 'G': 0}
    problem = GraphProblem('S', ['g', 'G'], graph_g, graph_h)
    return problem

def main():
    problem1 = make_graph_problem_cs561()

    print("="*10 + "\nBFS")
    path, expanded = breadth_first_graph_search(problem1)
    print("Expanded: ", expanded)
    print("Path: ", path)
    print("="*10 + "\nDFS")
    path, expanded = depth_first_graph_search(problem1)
    print("Expanded: ", expanded)
    print("Path: ", path)
    # print("="*10 + "\nGBFS")
    # greedy_best_first_graph_search(problem1)
    print("="*10 + "\nUCS")
    print(uniform_cost_search(problem1))
    print("="*10 + "\nA*")
    print(astar_search(problem1))

if __name__ == '__main__':
    main()