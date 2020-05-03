from token_types import SUM, MIN, DIV, MUL
from tokens_parser import Parser


class TreeProcessor():
    def __init__(self, code: str):
        self.parser = Parser(code)
        self.GLOBAL_SCOPE = {}

    def process(self, node):
        processor_name = 'process_{}'.format(type(node).__name__)
        processor = getattr(self, processor_name)

        return processor(node)


class Interpreter(TreeProcessor):
    def eval(self):
        tree = self.parser.parse()
        self.process(tree)
        return self.GLOBAL_SCOPE

    def process_UniNode(self, node):
        if node.op.type == SUM:
            return self.process(node.expr)
        elif node.op.type == MIN:
            return -1 * self.process(node.expr)

    def process_Assign(self, node):
        var_name = node.left.var
        self.GLOBAL_SCOPE[var_name] = self.process(node.right)

    def process_Compound(self, node):
        for child in node.children:
            self.process(child)

    def process_NoOp(self, node):
        pass

    def process_Var(self, node):
        val = self.GLOBAL_SCOPE.get(node.var)
        if val is None:
            raise NameError("NO node.var in scope")

        return val

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
