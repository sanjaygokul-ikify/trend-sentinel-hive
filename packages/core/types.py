from typing import List

class Policy:
    def __init__(self, name: str, rules: List['Rule']):
        self.name = name
        self.rules = rules

    def get_name(self):
        return self.name

    def get_rules(self):
        return self.rules

class Rule:
    def __init__(self, action: str, condition: str):
        self.action = action
        self.condition = condition

    def get_action(self):
        return self.action

    def get_condition(self):
        return self.condition

class Task:
    def __init__(self, action: str, condition: str):
        self.action = action
        self.condition = condition

    def get_action(self):
        return self.action

    def get_condition(self):
        return self.condition
