import heapq
from core.node import Node
from core.problem import Problem


def astar_search(problem : Problem) -> Node | None: 
    """
    A* Search
    f(n) = g(n) + h(n)
    """

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

        if problem.goal_test(node.state):
            return node
        
        for child in node.expand(problem):
            counter += 1
            f = child.path_cost + problem.heuristic(child.state)
            heapq.heappush(frontier, (f, counter, child))

    return None