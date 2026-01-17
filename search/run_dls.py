from search.uninformed.depth_limited_search import depth_limited_search
from search.problems.gridworld import GridWorld

def main():
    problem = GridWorld(
        initial_state=(0,0),
        goal_state=(2,2),
        width=3,
        height=3
    )

    for limit in range(1, 6):
        print(f"\nDepth limit = {limit}")
        result = depth_limited_search(problem, limit)

        if result == "cutoff":
            print("Cutoff occurred")
        elif result is None:
            print("No solution")
        else:
            print("Solution Found")
            print("Actions:", result.solution())
            print("Path:", [n.state for n in result.path()])

if __name__ == "__main__":
    main()