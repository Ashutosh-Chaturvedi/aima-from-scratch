from search.uninformed.ucs import uniform_cost_search
from search.problems.gridworld import GridWorld

def main():
    problem = GridWorld(
        initial_state=(0,0),
        goal_state=(2,2),
        width=3,
        height=3
    )

    solution = uniform_cost_search(problem)

    if solution:
        print("Solution Found!")
        print("Actions:", solution.solution())
        print("Path:", [n.state for n in solution.path()])
        print("Cost: ", solution.path_cost)
    else:
        print("No solution found.")
        
if __name__ == "__main__":
    main()