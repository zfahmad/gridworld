class Agent:
    def __init__(self, name: str):
        self.name = name
    
    def select_action(self, actions: list) -> str:
        pass

    def get_name(self):
        return self.name