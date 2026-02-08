from search.problems.erratic_vacuum import ErraticVacuumWorld
from search.nondeterministic.and_or_search import and_or_search

def print_plan(plan, indent=0):
    if plan == "DONE":
        print("  " * indent + "DONE")
        return

    action, branches = plan
    print("  " * indent + f"Action: {action}")

    for state, subplan in branches.items():
        print("  " * indent + f"If state == {state}:")
        print_plan(subplan, indent + 1)

problem = ErraticVacuumWorld()

initial = ("A", True, True)

plan = and_or_search(problem, initial)




print_plan(plan)