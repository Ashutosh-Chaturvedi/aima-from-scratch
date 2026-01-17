import argparse

from search.uninformed.bfs import breadth_first_search
from search.problems.gridworld import GridWorld

def parse_args():
    parser = argparse.ArgumentParser(
        description="Run BFS on a GridWorld problem."
    )

    parser.add_argument("--width", type=int, default=3)
    parser.add_argument("--height", type=int, default=3)

    parser.add_argument("--start", type=int, nargs=2, default=[0,0], metavar=("X", "Y"))

    parser.add_argument("--goal", type=int, nargs=2, default=[2,2], metavar=("X", "Y"))

    return parser.parse_args()

def main():

    args = parse_args()

    problem = GridWorld(
        initial_state=tuple(args.start),
        goal_state=tuple(args.goal),
        width=args.width, 
        height=args.height
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