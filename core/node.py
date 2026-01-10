from dataclasses import dataclass
from typing import Any, Optional, List

@dataclass
class Node: 
    state: Any
    parent: Optional["Node"] = None
    action: Optional[Any] = None
    path_cost: float = 0.0
    depth: int = 0

    def expand(self, problem) -> List["Node"]:
        """Return the list of child nodes reachable from this node. (Adjancent nodes)"""
        children = []

        for action in problem.actions(self.state):
            next_state = problem.result(self.state, action)
            cost = self.path_cost + problem.step_cost(
                self.state, action, next_state
            )

            child = Node(
                state=next_state, 
                parent=self, 
                action=action, 
                path_cost=cost, 
                depth=self.depth + 1
            )

            children.append(child)

        return children
    
    def path(self) -> List["Node"]:
        """Return the path from the root to this node."""
        node, path_back = self, []

        while node is not None:
            path_back.append(node)
            node = node.parent

        return list(reversed(path_back))
    
    def solution(self) -> List[Any]:
        """Return the sequence of actions to reach this node."""
        return [node.action for node in self.path()[1:]]