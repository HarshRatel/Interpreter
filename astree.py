from lexer_tokens import Token

class ASTNode():
    pass

class OpNode(ASTNode):
    def __init__(self, left : ASTNode, op : Token, right : ASTNode):
        self.left = left
        self.token = op
        self.val = op.val
        self.right = right

class NumNode(ASTNode):
    def __init__(self, token):
        self.token = token
        self.val = self.token.val

class UniNode(ASTNode):
    def __init__(self, token, expr):
        self.op = token
        self.expr = expr

class Compound(ASTNode):
    def __init__(self):
        self.children = []

class Assign(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.token = op
        self.right = right    

class Var(ASTNode):
    def __init__(self, token):
        self.var = token.val

class NoOp(ASTNode):
    def __init__(self):
        pass