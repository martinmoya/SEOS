"""
Code Knowledge.
Stores symbols extracted from any programming language.
"""


class CodeKnowledge:
    def __init__(self):
        self.symbols: list = []
        self.relations: list = []

    def add(self, symbol):
        self.symbols.append(symbol)

    def all(self):
        return self.symbols

    def add_relation(self, relation):
        self.relations.append(relation)

    def all_relations(self):
        return self.relations
