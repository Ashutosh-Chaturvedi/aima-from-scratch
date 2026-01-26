from core.problem import Problem


class EightPuzzle(Problem):
    GOAL_STATE = (0, 1, 2, 
                  3, 4, 5, 
                  6, 7, 8)

    def __init__(self, initial_state):
        super().__init__(initial_state)

    # ---------- Problem interface ----------

    def actions(self, state):
        actions = []
        blank = state.index(0)
        row, col = divmod(blank, 3)

        if row > 0:
            actions.append("UP")
        if row < 2:
            actions.append("DOWN")
        if col > 0:
            actions.append("LEFT")
        if col < 2:
            actions.append("RIGHT")

        return actions

    def result(self, state, action):
        blank = state.index(0)
        row, col = divmod(blank, 3)

        def swap(i, j):
            lst = list(state)
            lst[i], lst[j] = lst[j], lst[i]
            return tuple(lst)

        if action == "UP":
            return swap(blank, blank - 3)
        if action == "DOWN":
            return swap(blank, blank + 3)
        if action == "LEFT":
            return swap(blank, blank - 1)
        if action == "RIGHT":
            return swap(blank, blank + 1)

        raise ValueError("Invalid action")

    def goal_test(self, state):
        return state == self.GOAL_STATE

    def step_cost(self, state, action, result):
        return 1

    # ---------- Heuristics ----------

    def heuristic(self, state):
        """
        Manhattan distance heuristic
        """
        distance = 0
        for i, tile in enumerate(state):
            if tile == 0:
                continue
            goal_index = self.GOAL_STATE.index(tile)
            r1, c1 = divmod(i, 3)
            r2, c2 = divmod(goal_index, 3)
            distance += abs(r1 - r2) + abs(c1 - c2)
        return distance

    def misplaced_tiles(self, state):
        """
        Alternative weaker heuristic
        """
        return sum(
            1 for i, tile in enumerate(state)
            if tile != 0 and tile != self.GOAL_STATE[i]
        )
