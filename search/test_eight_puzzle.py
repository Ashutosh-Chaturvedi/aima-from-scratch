from search.problems.eight_puzzle import EightPuzzle
from search.informed.astar import astar_search
from search.informed.ida_star import ida_star_search
from search.uninformed.bfs import breadth_first_search
from search.uninformed.dfs import depth_first_search

initial = (1, 2, 3,
           4, 0, 6,
           7, 5, 8)

problem = EightPuzzle(initial)

def print_board(state):
    for i in range(0, 9, 3):
        row = state[i:i+3]
        print(" ".join(str(x) if x != 0 else "_" for x in row))
    print()

def extract_states(solution):
    return [node.state for node in solution.path()]

print("A*:")
solution, stats = astar_search(problem)
print("Moves:", len(solution.path()) - 1)
states = extract_states(solution)
for state in extract_states(solution):
    print_board(state)
print("Expanded:", stats.expanded)

print("\nIDA*:")
solution, stats = ida_star_search(problem)
print("Moves:", len(solution.path()) - 1)
states = extract_states(solution)
for state in extract_states(solution):
    print_board(state)
print("Expanded:", stats.expanded)

print("\nBFS:")
solution, stats = breadth_first_search(problem)
print("Moves:", len(solution.path()) - 1)
states = extract_states(solution)
for state in extract_states(solution):
    print_board(state)
print("Expanded:", stats.expanded)

print("\nDFS:")
solution, stats = depth_first_search(problem)
print("Moves:", len(solution.path()) - 1)
states = extract_states(solution)
for state in extract_states(solution):
    print_board(state)
print("Expanded:", stats.expanded)