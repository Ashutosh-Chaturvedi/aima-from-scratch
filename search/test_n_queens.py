from search.problems.n_queens import NQueens
from search.local_search.hill_climbing import hill_climbing

n = 8
problem = NQueens(n)

solution, conflicts = hill_climbing(problem)

print("Final state: ", solution)
print("Conflicts: ", conflicts)

