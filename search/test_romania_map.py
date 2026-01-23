"""
Test harness for search algorithms using the Romania map problem (AIMA). 

This scrips runs: 
- BFS, DFS, DLS, IDDFS
- UCS (Dijkstra)
- Greedy BFS
- A*
- Weighted A*
- Memory Bounded:
    - Beam Search
    - IDA*
    - RBFS
    - SMA*
- Bidirectional A*

and prints the resulting paths and cost for comparison.
"""

from search.informed.greedy_best_first import greedy_best_first_search
from search.informed.astar import astar_search
from search.informed.weighted_astar import weighted_astar_search
from search.informed.beam_search import beam_search
from search.informed.ida_star import ida_star_search
from search.informed.rbfs import rbfs_search
from search.informed.sma_star import sma_star_search
from search.informed.bidirectional_astar import bidirectional_astar_search


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
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nGreedy Best-First Search: ")
solution = greedy_best_first_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nBreadth First Search: ")
solution = breadth_first_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nUniform Cost Search (Dijkstra's): ")
solution = uniform_cost_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nDepth First Serach: ")
solution = depth_first_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nIterative depth first search: ")
solution = iterative_deepening_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nDepth limited Search: ")
solution = depth_limited_search(problem, limit=5)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost)  
else:
    print("No solution found")

print("\nBidirectional BFS: ")
solution = bidirectional_breadth_first_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nWeighted A* (w = 1.2): ")
solution = weighted_astar_search(problem, weight=1.2)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nWeighted A* (w = 2.0):")
solution = weighted_astar_search(problem, weight=2.0)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nBeam Search (widht = 2):")
solution = beam_search(problem, beam_width=2)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nBeam Search (widht = 3):")
solution = beam_search(problem, beam_width=3)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nIDA* search: ")
solution = ida_star_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost) 
else:
    print("No solution found")

print("\nRBFS:")
solution = rbfs_search(problem)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost)
else:
    print("No solution found")

print("\nSMA* (memory = 1):")
solution = sma_star_search(problem, memory_limit=1)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost)
else:
    print("No solution found")

print("\nSMA* (memory = 50):")
solution = sma_star_search(problem, memory_limit=50)
if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost)
else:
    print("No solution found")

print("\nBidirectional A*:")
solution = bidirectional_astar_search(problem)

if solution:
    print("Path:", [n.state for n in solution.path()])
    print("Cost:", solution.path_cost)
else:
    print("No solution found")
