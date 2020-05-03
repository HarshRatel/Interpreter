from token_types import *
from lexer import Lexer
from astree import OpNode, NumNode, UniNode, \
                    Compound, Assign, Var


class Parser():
    def __init__(self, code: str):
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

    def empty(self):
        return NoOp()

    def variable(self):
        node = Var(self.current_token)
        self.eat(ID)
        return node

    def assignment(self):
        '''
        assignment ::= variable ASSIGN expr
        '''
        left = self.variable()
        token = self.current_token()
        self.eat(ASSIGN)
        right = self.expr()
        
        return Assign(left, token, right)

    def statement(self):
        '''
         statement ::=  compound_statement
                        | assignment
                        | empty
        '''
        if self.current_token.type == BEGIN:
            return self.compound_statement()
        elif self.current_token.type == ID:
            return self.assignment()
        
        return self.empty()

    def statement_list(self):
        '''
        statement_list ::= statement | statement ; statement_list
        '''
        node = self.statement()
        
        results = [node]

        while self.current_token.type == SEMI:
            self.eat(SEMI)
            results.append(self.statement)
        
        if self.current_token.type == ID:
            self.error()

        return results
        
    def compound_statement(self):
        '''
        compound_statement ::= BEGIN statement_list END
        '''
        root = Compound()
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)

        for node in nodes:
            root.children.append(node)

        return root

    def program(self):
        '''
        program ::= compound_statement DOT
        '''
        node = self.compound_statement()
        self.eat(DOT)
        return node

    def parse(self):
        return self.expr()