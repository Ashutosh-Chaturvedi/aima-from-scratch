from core.node import Node
from core.problem import Problem
import math


def rbfs_search(problem: Problem):
    root = Node(problem.initial_state)
    root_f = problem.heuristic(root.state)
    result, _ = _rbfs(problem, root, root_f, math.inf)
    return result

def _rbfs(problem: Problem, node, node_f, f_limit):
    """
    Recursive Best-First Search
    """

    if problem.goal_test(node.state):
        return node, node_f
    
    successors = []

    for child in node.expand(problem):
        f = max(
            child.path_cost + problem.heuristic(child.state), node_f
        )
        successors.append((child, f))

    if not successors:
        return None, math.inf
    
    while True:
        successors.sort(key=lambda x: x[1])
        best, best_f = successors[0]

        if best_f > f_limit:
            return None, best_f
        
        alternative_f = successors[1][1] if len(successors) > 1 else math.inf

        result, new_f = _rbfs(
            problem, best, best_f, min(f_limit, alternative_f)
        )

        successors[0] = (best, new_f)

        if result is not None:
            return result, new_f