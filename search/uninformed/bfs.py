from collections import deque
from core.node import Node


def breadth_first_search(problem):
    root = Node(problem.initial_state)

    if problem.goal_test(root.state):
        return root

    frontier = deque([root])
    explored = set()

    while frontier:
        node = frontier.popleft()
        explored.add(node.state)

        for child in node.expand(problem):
            if (
                child.state not in explored
                and child.state not in (n.state for n in frontier)
            ):
                if problem.goal_test(child.state):
                    return child
                frontier.append(child)

    return None
