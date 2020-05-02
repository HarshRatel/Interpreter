from token_types import INT, EOF, SUM, MIN, DIV, MUL, LPAR, RPAR
from tokens_parser import Parser
from astree import OpNode, NumNode

class TreeProcesser():
    def __init__(self, code : str):
        self.parser = Parser(code)
    
    def process(self, node):
        processor_name = 'process_{}'.format(type(node).__name__)
        processor = getattr(self, processor_name)

        return processor(node)

class Interpreter(TreeProcesser):
    def eval(self):
        tree = self.parser.parse()
        
        return self.process(tree)

    def process_OpNode(self, node):
        if node.token.type == SUM:
            return self.process(node.left) + self.process(node.right)
        elif node.token.type == MIN:
            return self.process(node.left) - self.process(node.right)
        elif node.token.type == MUL:
            return self.process(node.left) * self.process(node.right)
        elif node.token.type == DIV:
            return self.process(node.left) / self.process(node.right)
    
    def process_NumNode(self, node):
        return node.val