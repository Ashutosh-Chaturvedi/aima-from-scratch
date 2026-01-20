from abc import ABC, abstractmethod
from typing import Any, Iterable

class Problem(ABC):
    """
    Abstract base class for a formal problem. 
    Every problem should inherit from this class and implement the abstract methods.
    """

    def __init__(self, initial_state: Any):
        self.initial_state = initial_state

    @abstractmethod
    def actions(self, state: Any) -> Iterable[Any]:
        """
        Return the actions that can be executed in the given state. 
        """
        pass

    @abstractmethod
    def result(self, state: Any, action: Any) -> Any:
        """
        Return the state that results from execution of action. 
        """
        pass

    @abstractmethod
    def goal_test(self, state: Any) -> bool:
        """
        Return True if the state statisfies the goal condition.
        """
        pass

    def step_cost(self, state: Any, action: Any, next_state: Any) -> float:
        """
        Return the cost of talking that action. 

        Default cost is 1. 
        Can override if needed. 
        """
        return 1.0
    
    def predecessors(self, state):
        """
        Return iterable of (prev_state, action) pairs that can lead to the given state. 

        Override if the problem supports backward search.
        """
        raise NotImplementedError
    
    def heuristic(self, state):
        """
        Estimated remaining cost from current state to goal state. 
        
        Override in problems that supports heuristic.
        """
        return 0
    
    