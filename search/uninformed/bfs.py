from collections import deque
from core.node import Node
from utils.search_stats import SearchStats

def breadth_first_search(problem):
    stats = SearchStats()

    root = Node(problem.initial_state)

    if problem.goal_test(root.state):
        return root, stats

    frontier = deque([root])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)
        stats.expanded += 1

        for child in node.expand(problem):
            if (
                child.state not in explored
                and child.state not in (n.state for n in frontier)
            ):
                if problem.goal_test(child.state):
                    return child, stats
                frontier.append(child)

    return None, stats
