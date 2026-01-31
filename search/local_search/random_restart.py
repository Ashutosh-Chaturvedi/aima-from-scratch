from search.local_search.hill_climbing import hill_climbing

def random_restart_hill_climbing(problem, max_restarts = 1000, max_steps = 1000):
    """
    Random-Restart Hill Climbing.

    Returns:
        (solution_state, conflicts, restarts_used)    
    """

    best_state = None
    best_conflicts = float("inf")

    for restart in range(max_restarts):
        state, conflicts = hill_climbing(problem, max_steps=max_steps)

        if conflicts == 0:
            return state, conflicts, restart + 1
        
        if conflicts < best_conflicts:
            best_state = state
            best_conflicts = conflicts

    return best_state, best_conflicts, max_restarts