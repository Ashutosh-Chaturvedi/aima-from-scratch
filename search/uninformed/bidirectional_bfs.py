from collections import deque
from core.node import Node
from core.problem import Problem

def _expand_frontier(frontier, explored_this, explored_other, problem):
    node = frontier.popleft()

    for child in node.expand(problem):
        if child.state in explored_this:
            continue

        explored_this[child.state] = child

        # Meeting point
        if child.state in explored_other:
            return child, explored_other[child.state]
        
        frontier.append(child)

    return None

def _expand_backward(frontier, explored_this, explored_other, problem: Problem):
    node = frontier.popleft()

    for prev_state, action in problem.predecessors(node.state):
        if prev_state in explored_this:
            continue

        child = Node(
            state=prev_state, 
            parent=node, 
            action=action, 
            path_cost=node.path_cost + 1, 
            depth=node.depth + 1
        )

        explored_this[prev_state] = child

        if prev_state in explored_other:
            return explored_other[prev_state], child
        
        frontier.append(child)

    return None

def _construct_path(meet_forward, meet_backward):
    """
    Combine forward and backward paths at meeting point.
    """

    # Forward path: start -> meeting
    path_f = meet_forward.path()

    # Backward path: goal -> meeting (reverse it)
    path_b = meet_backward.path()
    path_b.reverse()

    # Remove duplicate meeting node
    full_path = path_f + path_b[1:]

    # Return final node with full path reconstructed
    return full_path[-1]

def bidirectional_breadth_first_search(problem: Problem):
    """
    Bidirectional Breadth-First Search.
    Assumes reversible actions and a single explicit goal state.
    """

    if not hasattr(problem, "predecessors"):
        raise ValueError("Problem does not support backward search")

    start = problem.initial_state
    goal = problem.goal_state   

    if start == goal:
        return Node(start)
    
    # Frontiers
    frontier_f = deque([Node(start)])
    frontier_b = deque([Node(goal)])

    # Explored maps: state -> Node
    explored_f = {start: frontier_f[0]}
    explored_b = {goal: frontier_b[0]}

    while frontier_f and frontier_b:

        # Forward expansion
        result = _expand_frontier(frontier_f, explored_f, explored_b, problem)

        if result:
            return _construct_path(*result)
        
        # Backward expansion
        result = _expand_backward(frontier_b, explored_b, explored_f, problem)
        if result:
            return _construct_path(*result)
        
    return None