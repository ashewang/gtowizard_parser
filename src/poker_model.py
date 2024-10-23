from typing import List

class Action:
    def __init__(self, code: str, bet_size: str, position: str, history: str):
        self.code = code
        self.bet_size = bet_size
        self.position = position
        self.history = history
    
    def __str__(self):
        return f"{self.history},{self.code},{self.bet_size},{self.position}"

class Strategy:
    def __init__(self, actions: List[Action]):
        self.actions = actions
