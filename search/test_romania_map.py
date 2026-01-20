from search.informed.greedy_best_first import greedy_best_first_search
from search.informed.astar import astar_search

from search.uninformed.bfs import breadth_first_search
from search.uninformed.dfs import depth_first_search
from search.uninformed.dls import depth_limited_search
from search.uninformed.ucs import uniform_cost_search
from search.uninformed.iddfs import iterative_deepening_search
from search.uninformed.bidirectional_bfs import bidirectional_breadth_first_search

from search.problems.romania_map import RomaniaMap


problem = RomaniaMap("Arad")

print("A* Search: ")
solution = astar_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nGreedy Best-First Search: ")
solution = greedy_best_first_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nBreadth First Search: ")
solution = breadth_first_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nUniform Cost Search (Dijkstra's): ")
solution = uniform_cost_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nDepth First Serach: ")
solution = depth_first_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nIterative depth first search: ")
solution = iterative_deepening_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nDepth limited Search: ")
solution = depth_limited_search(problem, limit=5)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)

print("\nBidirectional BFS: ")
solution = bidirectional_breadth_first_search(problem)
print("Path:", [n.state for n in solution.path()])
print("Cost:", solution.path_cost)