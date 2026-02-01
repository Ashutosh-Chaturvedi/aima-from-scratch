import math 
import random

def simulated_annealing(problem, max_steps=100000, initial_temp=100.0, cooling_rate=0.995):
    """
    Simulated Annealing for local search. 

    Returns: 
        (final_state, conflicts)
    """

    current = problem.random_state()
    current_cost = problem.conflicts(current)

    T = initial_temp

    for step in range(max_steps):
        if current_cost == 0:
            return current, current_cost
        
        if T <= 1e-8:
            break

        # Pick a random neighbor
        neighbors = problem.neighbors(current)
        next_state = random.choice(neighbors)
        next_cost = problem.conflicts(next_state)

        delta = next_cost - current_cost

        if delta < 0: 
            current = next_state
            current_cost = next_cost
        else: 
            probability = math.exp(-delta / T)
            if random.random() < probability:
                current = next_state
                current_cost = next_cost

        T *= cooling_rate
    
    return current, current_cost