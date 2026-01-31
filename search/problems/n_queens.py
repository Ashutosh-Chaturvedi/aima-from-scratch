import random


class NQueens:
    def __init__(self, n):
        self.n = n

    def random_state(self):
        """
        Generate a random complete assignment.
        """
        return tuple(random.randint(0, self.n - 1) for _ in range(self.n))
    
    def conflicts(self, state):
        """
        Count number of attacking queen pairs.
        """
        conflicts = 0
        n = self.n

        for col1 in range(n):
            for col2 in range(col1 + 1, n):
                row1 = state[col1]
                row2 = state[col2]

                if row1 == row2:
                    conflicts += 1
                elif abs(row1 - row2) == abs(col1 - col2):
                    conflicts += 1
        
        return conflicts
    
    def neighbors(self, state):
        """
        Generate all neighboring state by moving one queen within its column.
        """
        neighbors = []

        for col in range(self.n):
            for row in range(self.n):
                if row != state[col]:
                    new_state = list(state)
                    new_state[col] = row
                    neighbors.append(tuple(new_state))

        return neighbors