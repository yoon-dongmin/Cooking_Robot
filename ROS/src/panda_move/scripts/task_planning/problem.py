class StripsProblem:
    def __init__(self, temp, using_ings = None):
        self.initial_state = temp[0]
        self.goal = temp[1]

class PlanningProblem:
    def __init__(self, domain, problem):
        """
        a planning problem consists of
        * a planning domain
        * the initial state
        * a goal 
        """
        self.prob_domain = domain
        self.initial_state = problem.initial
        self.goal = problem.goal