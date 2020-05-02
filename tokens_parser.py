from token_types import INT, EOF, SUM, MIN, DIV, MUL, LPAR, RPAR
from lexer import Lexer
from astree import OpNode, NumNode, UniNode

class Parser():
    def __init__(self, code : str):
        self.lexer = Lexer(code)
        self.current_token = self.lexer.get_token()
        
    def error(self):
        raise Exception("Failed parse input")

    def eat(self, right):
        if self.current_token.type == right:
            self.current_token = self.lexer.get_token()
        else:
            self.error()

    def factor(self):
        '''
        factor ::= (PLUS | MINUS) factor | INTEGER | LPAR expression RPAR
        '''
        if self.current_token.type == SUM:
            op = self.current_token
            self.eat(SUM)
            return UniNode(op, self.factor())
        elif self.current_token.type == MIN:
            op = self.current_token
            self.eat(MIN)
            return UniNode(op, self.factor())
        elif self.current_token.type == INT:
            node = NumNode(self.current_token)
            self.eat(INT)
            return node
        elif self.current_token.type == LPAR:
            self.eat(LPAR)
            node = self.expr()
            self.eat(RPAR)
            return node

    def term(self):
        '''
        term ::= factor ((SUM | MIN) factor)*
        '''
        node = self.factor()

        while self.current_token.type in [MUL, DIV]:
            op = self.current_token
            if self.current_token.val == '*':
                self.eat(MUL)
            elif self.current_token.val == '/':
                self.eat(DIV)
                
            node = OpNode(node, op, self.factor())

        return node

    def expr(self):
        '''
        expr ::= term ((MUL | DIV) term)*
        '''
        node = self.term()

        while self.current_token.type in [SUM, MIN]:
            op = self.current_token
            if self.current_token.val == '+':
                self.eat(SUM)           
            elif self.current_token.val == '-':
                self.eat(MIN)
            
            node = OpNode(node, op, self.term())
            
        return node

    def parse(self):
        return self.expr()