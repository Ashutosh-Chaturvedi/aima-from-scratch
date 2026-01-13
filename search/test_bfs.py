from search.uninformed.breadth_first_search import breadth_first_search
from search.problems.gridworld import GridWorld

def main():
    problem = GridWorld(
        initial_state=(0,0),
        goal_state=(2,2),
        width=3, 
        height=3
    )

    solution_node = breadth_first_search(problem)

    if solution_node:
        print("Solution found!")
        print("Actions:", solution_node.solution())
        print("Path:", [node.state for node in solution_node.path()])
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()