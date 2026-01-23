import heapq
import math
from core.node import Node
from core.problem import Problem


def bidirectional_astar_search(problem: Problem):
    """
    Bidirectional A* Search
    """

    start = Node(problem.initial_state)
    goal = Node(problem.goal_state)

    frontier_f = []
    frontier_b = []

    heapq.heappush(frontier_f, (problem.heuristic(start.state), start))
    heapq.heappush(frontier_b, (problem.heuristic(goal.state), goal))

    explored_f = {}
    explored_b = {}

    best_cost = math.inf
    meeting_node_f = None
    meeting_node_b = None

    while frontier_f and frontier_b:

        # Forward step
        f_f, node_f = heapq.heappop(frontier_f)

        if node_f.state in explored_f:
            continue

        explored_f[node_f.state] = node_f

        if node_f.state in explored_b:
            cost = node_f.path_cost + explored_b[node_f.state].path_cost
            if cost < best_cost:
                best_cost = cost
                meeting_node_f = node_f
                meeting_node_b = explored_b[node_f.state]

        for child in node_f.expand(problem):
            f = child.path_cost + problem.heuristic(child.state)
            heapq.heappush(frontier_f, (f, child))

        # Backward step
        f_b, node_b = heapq.heappop(frontier_b)

        if node_b.state in explored_b:
            continue

        explored_b[node_b.state] = node_b

        if node_b.state in explored_f:
            cost = node_b.path_cost + explored_f[node_b.state].path_cost
            if cost < best_cost:
                best_cost = cost
                meeting_node_f = explored_f[node_b.state]
                meeting_node_b = node_b

        for child in expand_backward(node_b, problem):
            f = child.path_cost + problem.heuristic(child.state)
            heapq.heappush(frontier_b, (f, child))

        # Optimality stopping condition
        if frontier_f and frontier_b:
            if frontier_f[0][0] + frontier_b[0][0] >= best_cost:
                break

    if meeting_node_f and meeting_node_b:
        return _reconstruct_bidirectional_path(
            meeting_node_f,
            meeting_node_b
        )

    return None

def _reconstruct_bidirectional_path(node_f, node_b):
    """
    Reconstructs full path from start → goal
    """

    path_f = node_f.path()
    path_b = node_b.path()
    path_b.reverse()

    full_path = path_f + path_b[1:]

    root = full_path[0]
    current = root

    for next_node in full_path[1:]:
        next_node.parent = current
        current = next_node

    return current

def expand_backward(node, problem):
    """
    Generate predecessor nodes for backward search
    """
    for prev_state, action, cost in problem.predecessors(node.state):
        yield Node(
            state=prev_state,
            parent=node,
            action=action,
            path_cost=node.path_cost + cost,
            depth=node.depth + 1
        )
