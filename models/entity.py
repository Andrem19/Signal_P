from datetime import datetime
class Entity:
    def __init__(self, name):
        self.name: str = name
        self.info: dict = {}