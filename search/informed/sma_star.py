import heapq
import math
from core.node import Node


class SMAStarNode:
    """
    Wrapper node for SMA* to track f-values and children
    """
    def __init__(self, node, f):
        self.node = node
        self.f = f
        self.children = []
        self.parent = None

    def __lt__(self, other):
        return self.f < other.f


def sma_star_search(problem, memory_limit=50):
    """
    Simplified Memory-Bounded A*
    """

    root = Node(problem.initial_state)
    f_root = problem.heuristic(root.state)
    root_wrap = SMAStarNode(root, f_root)

    frontier = [root_wrap]
    heapq.heapify(frontier)

    all_nodes = [root_wrap]  # crude memory tracking

    while frontier:
        current = heapq.heappop(frontier)

        if problem.goal_test(current.node.state):
            return current.node

        # Expand node
        for child in current.node.expand(problem):
            f = child.path_cost + problem.heuristic(child.state)
            wrapped = SMAStarNode(child, f)
            wrapped.parent = current
            current.children.append(wrapped)

            heapq.heappush(frontier, wrapped)
            all_nodes.append(wrapped)

            # Enforce memory limit
            if len(all_nodes) > memory_limit:
                _forget_worst(all_nodes, frontier)

    return None


def _forget_worst(all_nodes, frontier):
    """
    Remove the node with the highest f-value
    """
    worst = max(all_nodes, key=lambda n: n.f)
    all_nodes.remove(worst)

    if worst in frontier:
        frontier.remove(worst)
        heapq.heapify(frontier)

    # Backup f-value to parent
    if worst.parent:
        worst.parent.f = max(
            worst.parent.f,
            worst.f
        )
