from search.problems.n_queens import NQueens
from search.local_search.hill_climbing import hill_climbing
from search.local_search.random_restart import random_restart_hill_climbing
from search.local_search.simulated_annealing import simulated_annealing
from search.local_search.local_beam_search import local_beam_search

n = 8
problem = NQueens(n)

solution, conflicts = hill_climbing(problem)

print("Final state: ", solution)
print("Conflicts: ", conflicts)

solution, conflicts, restart = random_restart_hill_climbing(problem)

print("Final state: ", solution)
print("Conflicts: ", conflicts)
print("Restarts used: ", restart)

state, conflicts = simulated_annealing(problem)

print("Final state:", state)
print("Conflicts:", conflicts)

state, conflicts = local_beam_search(problem, k=10000)

print("Final state:", state)
print("Conflicts:", conflicts)