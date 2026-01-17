from core.node import Node
from core.problem import Problem

def depth_limited_search(problem: Problem, limit):
    """
    Depth-Limited Search (DLS).
    DFS with a maximum depth limit.
    """

    def recursive_dls(node, problem: Problem, limit):
        if problem.goal_test(node.state):
            return node
        
        if limit == 0:
            return "cutoff"
        
        cutoff_occurred = False

        for child in node.expand(problem):
            result = recursive_dls(child, problem, limit-1)

            if result == "cutoff":
                cutoff_occurred = True
            elif result is not None:
                return result
            
        if cutoff_occurred:
            return "cutoff"
        else:
            return None
        
    root = Node(problem.initial_state)
    return recursive_dls(root, problem, limit)