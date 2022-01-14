#-*- encoding: utf-8 -*-
class Arc:
    def __init__(self, from_node, to_node, cost=1, action=None):
        assert cost >= 0, ("Cost cannot be negative for {}->{}, cost:{}").format(from_node, to_node, cost)
        self.from_node = from_node
        self.to_node = to_node
        self.action = action
        self.cost = cost

    def __repr__(self):
        """ arc를 string 형태로 표현 """
        if self.action:
            return str(self.action)
        else:
            return 'None'

def zero(*args, **nargs):
    """ 항상 0을 return """
    return 0

class ForwardPlanner:
    def __init__(self, domain, problem, heur=zero):
        self.prob_domain = domain
        self.initial_state = problem.initial_state
        self.goal = problem.goal
        self.heur = heur
    
    def is_goal(self, state):
        """ 주어진 state가 goal이면 True를 반환 """
        return all(state[prop] == self.goal[prop] for prop in self.goal if prop in state)

    def start_node(self):
        """ 주어진 start node를 반환 """
        return self.initial_state

    def neighbors(self, state):
        """ 주어진 state의 neighbor를 반환 """
        neighbors = []
        for act in self.prob_domain.get_actions():
            if self.possible(act, state):
                neighbors.append(Arc(state, self.effect(act, state), act.cost, act))
        return neighbors

    def possible(self, act, state_asst):
        """ 주어진 state에서 act가 possible 하면 True를 반환 """
        return act.preconds(state_asst)

    def effect(self, act, state_asst):
        """ 주어진 state_asst에서 act를 하는 것의 effect(state)를 반환 
        state_asst에 effect의 asst을 추가하여 state생성 """
        return act.effects(state_asst)

    def heuristic(self, state):
        """ heuristic은 state에서 goal까지 cost의 (under)estimate value """
        # self.heur(state.assignment, self.goal)
        return 0

class BackwardPlanner():
    def __init__(self):
        pass