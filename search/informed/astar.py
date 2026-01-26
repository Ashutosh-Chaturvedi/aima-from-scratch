import heapq
from core.node import Node
from core.problem import Problem
from utils.search_stats import SearchStats


def astar_search(problem : Problem): 
    """
    A* Search
    f(n) = g(n) + h(n)
    """

    stats = SearchStats()
    frontier = []
    counter = 0

    root = Node(problem.initial_state)
    f = root.path_cost + problem.heuristic(root.state)

    heapq.heappush(frontier, (f, counter, root))
    explored = {}

    while frontier:
        _, _, node = heapq.heappop(frontier)

        # Optimality condition
        if node.state in explored and explored[node.state] <= node.path_cost:
            continue

        explored[node.state] = node.path_cost
        stats.expanded += 1

        if problem.goal_test(node.state):
            return node, stats
        
        for child in node.expand(problem):
            counter += 1
            f = child.path_cost + problem.heuristic(child.state)
            heapq.heappush(frontier, (f, counter, child))

    return None, stats