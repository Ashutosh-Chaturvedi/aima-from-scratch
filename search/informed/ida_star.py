from core.node import Node
from core.problem import Problem
import math
from utils.search_stats import SearchStats


def ida_star_search(problem: Problem):
    """
    Iterative Deepening A* (IDA*)
    """

    stats = SearchStats()

    root = Node(problem.initial_state)
    threshold = problem.heuristic(root.state)

    while True:
        result, new_threshold = _dfs_contour(
            problem, 
            root, 
            threshold, stats
        )

        if result is not None:
            return result, stats
        
        if new_threshold == math.inf:
            return None, stats
        
        threshold = new_threshold

def _dfs_contour(problem: Problem, node, threshold, stats):
    """
    Depth-first search with f-cost cutoff
    """
    stats.expanded += 1

    f = node.path_cost + problem.heuristic(node.state)

    if f > threshold:
        return None, f
    
    if problem.goal_test(node.state):
        return node, threshold
    
    min_excess = math.inf

    for child in node.expand(problem):
        result, excess = _dfs_contour(
            problem, 
            child,
            threshold, stats
        )

        if result is not None:
            return result, threshold
        
        min_excess = min(min_excess, excess)

    return None, min_excess