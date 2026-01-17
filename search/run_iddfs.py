from search.uninformed.iddfs import iterative_deepening_search
from search.problems.gridworld import GridWorld


def main():
    problem = GridWorld(
        initial_state=(0, 0),
        goal_state=(2, 2),
        width=3,
        height=3
    )

    result = iterative_deepening_search(problem)

    if result:
        print("Solution found")
        print("Actions:", result.solution())
        print("Path:", [n.state for n in result.path()])
        print("Depth:", result.depth)
    else:
        print("No solution found")


if __name__ == "__main__":
    main()
