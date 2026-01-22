from core.node import Node
from core.problem import Problem


def beam_search(problem: Problem, beam_width: int):
    """
    Beam Search (memory-bounded BFS variant)

    Keeps only the top `beam_width` nodes at each depth, 
    ranked by heuristic value. 
    """

    # Start with root
    frontier = [Node(problem.initial_state)]

    while frontier:
        next_frontier = []

        for node in frontier:
            if problem.goal_test(node.state):
                return node
            
            for child in node.expand(problem):
                next_frontier.append(child)

        if not next_frontier:
            return None
        
        # Rank by heuristic (lower is better)
        next_frontier.sort(
            key=lambda n: problem.heuristic(n.state)
        )

        # Keep only best K nodes
        frontier = next_frontier[:beam_width]

    return None

