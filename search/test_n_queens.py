from search.problems.n_queens import NQueens
from search.local_search.hill_climbing import hill_climbing
from search.local_search.random_restart import random_restart_hill_climbing

n = 8
problem = NQueens(n)

solution, conflicts = hill_climbing(problem)

print("Final state: ", solution)
print("Conflicts: ", conflicts)

solution, conflicts, restart = random_restart_hill_climbing(problem)

print("Final state: ", solution)
print("Conflicts: ", conflicts)
print("Restarts used: ", restart)

