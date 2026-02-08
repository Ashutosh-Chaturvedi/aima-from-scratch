def and_or_search(problem, state):
    memo = {}
    return or_search(problem, state, memo)


def or_search(problem, state, memo):
    if problem.is_goal(state):
        return "DONE"

    if state in memo:
        return memo[state]

    for action in problem.actions(state):
        plan = and_search(problem, state, action, memo)
        if plan is not None:
            memo[state] = (action, plan)
            return memo[state]

    memo[state] = None
    return None


def and_search(problem, state, action, memo):
    plans = {}

    for outcome in problem.results(state, action):
        subplan = or_search(problem, outcome, memo)
        if subplan is None:
            return None
        plans[outcome] = subplan

    return plans
