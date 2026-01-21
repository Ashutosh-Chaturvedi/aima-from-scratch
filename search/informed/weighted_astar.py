import heapq
from core.node import Node
from core.problem import Problem


def weighted_astar_search(problem : Problem, weight = 1.5) -> Node | None: 
    """
    Weighted A* Search
    f(n) = g(n) + weight * h(n)

    weight = 1.0 -> standard A*\n
    weight > 1.0 -> faster, suboptimal (not the best possible solution)
    """

    frontier = []
    counter = 0

    root = Node(problem.initial_state)
    f = root.path_cost + weight * problem.heuristic(root.state)

    heapq.heappush(frontier, (f, counter, root))

    explored = {}

    while frontier:
        _, _, node = heapq.heappop(frontier)

        # Optimality condition
        if node.state in explored and explored[node.state] <= node.path_cost:
            continue

        explored[node.state] = node.path_cost

        if problem.goal_test(node.state):
            return node
        
        for child in node.expand(problem):
            counter += 1
            f = child.path_cost + weight * problem.heuristic(child.state)
            heapq.heappush(frontier, (f, counter, child))

    return None