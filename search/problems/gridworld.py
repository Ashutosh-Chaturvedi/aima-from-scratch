from typing import Any
from core.problem import Problem

class GridWorld(Problem):

    def __init__(self, initial_state, goal_state, height, width):
        super().__init__(initial_state)
        self.goal_state = goal_state
        self.height = height
        self.width = width

    def actions(self, state):
        x, y = state
        actions = []

        if x > 0: 
            actions.append("LEFT")
        if x < self.width - 1:
            actions.append("RIGHT")
        if y > 0:
            actions.append("UP")
        if y < self.height - 1:
            actions.append("DOWN")

        return actions 
    
    def result(self, state, action):
        x, y = state

        if action == "LEFT":
            return (x-1, y)
        if action == "RIGHT":
            return (x+1, y)
        if action == "UP":
            return (x, y-1)
        if action == "DOWN":
            return (x, y+1)
        
        raise ValueError(f"Unknown action: {action}")
    
    def goal_test(self, state):
        # print("Checking goal:", state)
        return state == self.goal_state
