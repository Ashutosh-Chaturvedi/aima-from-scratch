import random 

def genetic_algorithm(
        problem, 
        population_size=100, 
        generations=1000, 
        mutation_rate=0.1
):
    """
    Genetic Algorithm for N-Queens. 
    Returns: 
        (solution_state, conflicts)
    """

    # Helper functions

    def fitness(state):
        # Higher is better
        return -problem.conflicts(state)
    
    def select(population):
        # Tournament selection 
        a, b = random.sample(population, 2)
        return a if fitness(a) > fitness(b) else b
    
    def crossover(parent1, parent2):
        n = problem.n
        point = random.randint(1, n-1)
        return parent1[:point] + parent2[point:]
    
    def mutate(state):
        n = problem.n 
        if random.random() < mutation_rate:
            col = random.randint(0, n-1)
            row = random.randint(0, n-1)
            lst = list(state)
            lst[col] = row
            return tuple(lst)
        return state
    

    # Initialize population 
    population = [problem.random_state() for _ in range(population_size)]

    # Evolution Loop 
    for gen in range(generations):
        population.sort(key=fitness, reverse=True)

        # Check for solution 
        best = population[0]
        best_conflicts = problem.conflicts(best)
        if best_conflicts == 0:
            return best, 0
        
        new_population = []

        # Elitism: keep top 10%
        elite_size = population_size // 10
        new_population.extend(population[:elite_size])

        # Generate rest
        while len(new_population) < population_size:
            parent1 = select(population)
            parent2 = select(population)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    # Return best found 
    population.sort(key=fitness, reverse=True)
    best = population[0]
    return best, problem.conflicts(best)

