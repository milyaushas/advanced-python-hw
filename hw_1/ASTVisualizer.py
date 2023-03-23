import ast
import networkx as nx
import os


class ASTVisualizer(ast.NodeVisitor):
    def __init__(self, filename):
        self.graph = nx.DiGraph()
        with open(filename, 'r') as file:
            self.root = ast.parse(file.read())

    def dfs(self):
        self.visit(self.root)

    def draw_result(self):
        nx.drawing.nx_agraph.to_agraph()