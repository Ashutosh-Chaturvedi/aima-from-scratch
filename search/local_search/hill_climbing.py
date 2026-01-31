def hill_climbing(problem, max_steps = 1000):
    """
    Steepest-ascent hill climbing.
    Return final state and its conflict count.
    """

    current = problem.random_state()
    current_cost = problem.conflicts(current)

    for step in range(max_steps):
        neighbors = problem.neighbors(current)

        next_state = current
        next_cost = current_cost

        for neighbor in neighbors:
            cost = problem.conflicts(neighbor)
            if cost < next_cost:
                next_state = neighbor
                next_cost = cost

        if next_cost >= current_cost:
            # No improvement
            return current, current_cost
        
        current = next_state
        current_cost = next_cost

    return current, current_cost
