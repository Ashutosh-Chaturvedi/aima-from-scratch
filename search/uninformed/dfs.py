from core.node import Node
from core.problem import Problem
from utils.search_stats import SearchStats


def depth_first_search(problem: Problem):
    """
    Expands the deepest node first.
    """
    stats = SearchStats()

    root = Node(problem.initial_state)

    if problem.goal_test(root.state):
        return root, stats

    frontier = [root]       # stack (LIFO)
    explored = set()

    while frontier:
        node = frontier.pop()

        if node.state in explored:
            continue

        explored.add(node.state)
        stats.expanded += 1

        for child in node.expand(problem):
            if child.state not in explored:
                if problem.goal_test(child.state):
                    return child, stats
                frontier.append(child)

    return None, stats
