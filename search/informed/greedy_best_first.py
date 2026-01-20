import heapq
from core.node import Node
from core.problem import Problem

def greedy_best_first_search(problem: Problem) -> Node | None:
    """
    Greedy Best-First Search
    f(n) = h(n) 
    where h(n) is a heuristic function. 
    """

    frontier = []
    counter = 0

    root = Node(problem.initial_state)
    h = problem.heuristic(root.state)

    heapq.heappush(frontier, (h, counter, root))
    explored = set()

    while frontier:
        _, _, node = heapq.heappop(frontier)

        if problem.goal_test(node.state):
            return node
        
        explored.add(node.state)

        for child in node.expand(problem):
            if child.state not in explored:
                counter += 1
                h = problem.heuristic(child.state)
                heapq.heappush(frontier, (h, counter, child))

    return None
