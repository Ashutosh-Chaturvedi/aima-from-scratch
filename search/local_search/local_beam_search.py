def local_beam_search(problem, k=5, max_steps=1000):
    """
    Local Beam Search. 

    Returns: 
        (best_state, conflicts)
    """

    # Start with k random states 
    states = [problem.random_state() for _ in range(k)]
    costs = [problem.conflicts(s) for s in states]

    for step in range(max_steps):
        # Check for solution 
        for state, cost in zip(states, costs):
            if cost == 0:
                return state, cost
            
        # Generaate all successors
        all_candidates = []

        for state in states: 
            for neighbor in problem.neighbors(state):
                cost = problem.conflicts(neighbor)
                all_candidates.append((cost, neighbor))

        # Keep k best states 
        all_candidates.sort(key=lambda x: x[0])
        states = [state for _, state in all_candidates[:k]]
        costs = [problem.conflicts(s) for s in states]

    # Return best found 
    best_index = costs.index(min(costs))
    return states[best_index], costs[best_index]