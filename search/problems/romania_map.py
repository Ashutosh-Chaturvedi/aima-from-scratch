from core.problem import Problem
from typing import Any, Iterable

class RomaniaMap(Problem):
    """
    Map of Romania problem from AIMA.
    States are city names.
    """

    def __init__(self, initial_state, goal_state = "Bucharest"):
        super().__init__(initial_state)
        self.goal_state = goal_state

        # Road distances (undirected graph)
        self.graph = {
            "Arad": {
                "Zerind": 75, 
                "Sibiu": 140, 
                "Timisoara": 118, 
            }, 
            "Zerind": {
                "Oradea": 71, 
                "Arad": 75,
            },
            "Oradea": {
                "Zerind": 71, 
                "Sibiu": 151,
            },
            "Sibiu": {
                "Arad": 140, 
                "Oradea": 151, 
                "Fagaras": 99, 
                "Rimnicu Vilcea": 80,
            },
            "Timisoara": {
                "Arad": 118, 
                "Lugoj": 111,
            }, 
            "Lugoj": {
                "Timisoara": 111, 
                "Mehadia": 70,
            }, 
            "Mehadia": {
                "Lugoj": 70, 
                "Drobeta": 75,
            }, 
            "Drobeta": {
                "Mehadia": 75, 
                "Craiova": 120,
            }, 
            "Craiova": {
                "Drobeta": 120, 
                "Pitesti": 138, 
                "Rimnicu Vilcea": 146,
            },
            "Rimnicu Vilcea": {
                "Sibiu": 80, 
                "Pitesti": 97,
                "Craiova": 146,
            },
            "Fagaras": {
                "Sibiu": 99,
                "Bucharest": 211,
            },
            "Pitesti": {
                "Rimnicu Vilcea": 97,
                "Craiova": 138,
                "Bucharest": 101,
            },
            "Bucharest": {
                "Fagaras": 211,
                "Pitesti": 101,
                "Giurgiu": 90,
                "Urziceni": 85,
            },
            "Giurgiu": {
                "Bucharest": 90,
            },
            "Urziceni": {
                "Bucharest": 85,
                "Hirsova": 98,
                "Vaslui": 142,
            },
            "Hirsova": {
                "Urziceni": 98,
                "Eforie": 86,
            },
            "Eforie": {
                "Hirsova": 86,
            },
            "Vaslui": {
                "Urziceni": 142,
                "Iasi": 92,
            },
            "Iasi": {
                "Vaslui": 92,
                "Neamt": 87,
            },
            "Neamt": {
                "Iasi": 87,
            },
        }

        self.coordinates = {
            "Arad": (91, 492),
            "Bucharest": (400, 327),
            "Craiova": (253, 288),
            "Drobeta": (165, 299),
            "Eforie": (562, 293),
            "Fagaras": (305, 449),
            "Giurgiu": (375, 270),
            "Hirsova": (534, 350),
            "Iasi": (473, 506),
            "Lugoj": (165, 379),
            "Mehadia": (168, 339),
            "Neamt": (406, 537),
            "Oradea": (131, 571),
            "Pitesti": (320, 368),
            "Rimnicu Vilcea": (233, 410),
            "Sibiu": (207, 457),
            "Timisoara": (94, 410),
            "Urziceni": (456, 350),
            "Vaslui": (509, 444),
            "Zerind": (108, 531),
        }


    def actions(self, state: Any) -> Iterable[Any]:
        return list(self.graph[state].keys())
    
    def result(self, state: Any, action: Any) -> Any:
        return action
    
    def goal_test(self, state: Any) -> bool:
        return state == self.goal_state
    
    def step_cost(self, state: Any, action: Any, next_state: Any) -> float:
        return self.graph[state][next_state]
    
    def heuristic(self, state):
        x1, y1 = self.coordinates[state]
        x2, y2 = self.coordinates[self.goal_state]
        return ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

    def predecessors(self, state):
        """
        Needed for bidirectional search. 
        Since the graph is undirected, predecessors = neighbors.
        """
        preds = []
        for city, neighbors in self.graph.items():
            if state in neighbors:
                cost = neighbors[state]
                action = f"{city}->{state}"
                preds.append((city, action, cost))

        return preds