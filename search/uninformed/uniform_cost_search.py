import heapq
from core.node import Node

def uniform_cost_search(problem):
    """
    Uniform-Cost Search (Dijkstra's algorithm). 
    Expands the node with the lowest path cost first. 
    """

    # Priority queue entries: (path_cost, tie_breaker, node)
    frontier = []
    counter = 0  # tie-breaker to avoid comparing Node objects

    root = Node(problem.initial_state)
    heapq.heappush(frontier, (root.path_cost, counter, root))

    explored = dict()   # state -> lowest cost found so far

    while frontier:
        _, _, node = heapq.heappop(frontier)

        # If we have already found a cheaper way to this state, skip it
        if node.state in explored and explored[node.state] <= node.path_cost:
            continue

        explored[node.state] = node.path_cost

        if problem.goal_test(node.state):
            return node
        
        for child in node.expand(problem):
            counter += 1
            heapq.heappush(
                frontier, 
                (child.path_cost, counter, child)
            )

    return None

