class ErraticVacuumWorld:
    def actions(self, state):
        return ["LEFT", "RIGHT", "SUCK"]

    def is_goal(self, state):
        _, dirt_a, dirt_b = state
        return not dirt_a and not dirt_b

    def results(self, state, action):
        loc, dirt_a, dirt_b = state

        if action == "LEFT":
            return {("A", dirt_a, dirt_b)}

        if action == "RIGHT":
            return {("B", dirt_a, dirt_b)}

        if action == "SUCK":
            if loc == "A":
                return {
                    ("A", False, dirt_b),   # success
                    ("A", dirt_a, dirt_b),  # failure
                }
            else:
                return {
                    ("B", dirt_a, False),
                    ("B", dirt_a, dirt_b),
                }

        raise ValueError(action)
