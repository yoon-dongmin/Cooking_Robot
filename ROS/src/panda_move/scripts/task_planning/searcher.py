#-*- encoding: utf-8 -*-
import heapq
import logging
from copy import deepcopy
from planner import ForwardPlanner

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
        """ arc에 포함 되어 있는 모든 node들을 반환 """
        current = self
        while current.arc is not None:
            yield current.arc.to_node
            current = current.initial
        yield current.initial

    def initial_node(self):
        """ initial node를 반환 """
        if self.arc is not None:
            for nd in self.initial.node(): yield nd
    
    def to_str(self):
        """ arc를 string으로 바꾸어서 반환 """
        if self.arc is None:
            return ""
        else:
            return str(self.initial)+" -> "+str(self.arc)

    def __repr__(self):
        """ arc를 string으로 표현 """
        if self.arc is None:
            return ""
        else:
            return str(self.initial)+" -> "+str(self.arc)
    
    def __len__(self):
        return len(list(self.nodes()))
    

class FrontierPQ:
    def __init__(self):
        self.frontier_index = 0
        self.frontierpq = []

    def empty(self):
        """ priority queue가 empty면 True를 반환 """
        return self.frontierpq == []

    def add(self, path, value):
        """ priority queue에 path를 add, value를 기준으로 sort """
        self.frontier_index += 1
        heapq.heappush(self.frontierpq, (value, -self.frontier_index, path))

    def pop(self):
        """ 최소의 value를 가지는 frontier의 path를 제거하여 반환 """
        (_, _, path) = heapq.heappop(self.frontierpq)
        return path

    def count(self, val):
        """ frontier에 있는 element 중 val과 동일한 value를 가지는 수를 반환 """
        return sum(1 for e in self.frontierpq if e[0] == val)

    def __repr__(self):
        return str([str(p) for (n,c,p) in self.frontierpq])

    def __len__(self):
        NotImplementedError

    def __iter__(self):
        NotImplementedError


class AStarSearcher:
    def __init__(self, problem):
        self.problem = problem
        self.num_expanded = 0
        self.explored = set()
        self.solution = Path(None)
        
        self.initialize_frontier()
        self.add_to_frontier(Path(problem.start_node()))
    
    def initialize_frontier(self):
        """ Priority Queue를 초기화 """
        self.frontier = FrontierPQ()

    def empty_frontier(self):
        """ 빈 Priority Queue를 반환 """
        return self.frontier.empty()

    def add_to_frontier(self, path):
        """ 기존 Priority Queue에 새로운 arc를 add """
        value = path.cost + self.problem.heuristic(path.end())
        self.frontier.add(path, value)

    def search(self, logger=None):
        """ goal에 도달하면 True 아니면 False을 return """
        while not self.empty_frontier():
            path = self.frontier.pop()
            self.num_expanded += 1            
            
            # path의 길이가 6 초과가 되면 Fail이라고 가정하고 False를 return
            if len(path) > 6:
                print("failed!!!! {}, {}".format(self.num_expanded, len(path)))
                return False
            
            # path의 마지막 node가 goal state과 동일할 경우 Success 이므로 True를 return
            if self.problem.is_goal(path.end()):
                print('goal!!!!!! {}'.format(path))
                self.solution = path
                return True
            else:
                neighs = self.problem.neighbors(path.end())
                for arc in neighs:
                    self.add_to_frontier(Path(path, arc))