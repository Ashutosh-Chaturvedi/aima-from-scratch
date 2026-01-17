from core.node import Node
from core.problem import Problem

def depth_first_search(problem: Problem):
    """
    Expands the deepest node first. 
    """

    root = Node(problem.initial_state)

    if problem.goal_test(root.state):
        return root
    
    frontier = [root]       # stack (LIFO)
    explored = set()

    while frontier:
        node = frontier.pop()
        explored.add(node.state)

        for child in node.expand(problem):
            if(
                child.state not in explored 
                and child.state not in (n.state for n in frontier)
            ):
                if problem.goal_test(child.state):
                    return child
                
                frontier.append(child)

    return Node
    