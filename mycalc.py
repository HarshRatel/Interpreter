INT, EOF, SUM, MIN, DIV, MUL, LPAR, RPAR = 'INT', 'EOF', 'SUM', 'MIN', 'DIV', 'MUL', 'LPAR', 'RPAR' 

class Token():
    def __init__(self, token_type, val = None):
        self.type = token_type
        self.val =  val

    def __str__(self):
        return "Token ({}, {})".format(self.type, self.val)

    def __repr__(self):
        return self.__str__()

class Lexer():
    def __init__(self, code : str):
        self.code = "".join([s for s in code if s != ' '])
        self.pos = 0
        self.current_char = self.code[self.pos]

    def step(self):
        self.pos += 1
        if self.pos < len(self.code):
            self.current_char = self.code[self.pos]
        else:
            self.current_char = None

    def process_int(self) -> int:
        digit = ''
        while self.current_char is not None and self.current_char.isdigit():
            digit += self.current_char
            self.step()

        return int(digit)

    def get_token(self):
        if self.current_char is None:
            self.current_token = Token(EOF)
            return self.current_token

        if self.current_char.isdigit():
            self.current_token = Token(INT, self.process_int())
            return self.current_token
        
        if self.current_char == '+':
            self.current_token = Token(SUM, '+')
            self.step()
            return self.current_token

        if self.current_char == '-':
            self.current_token = Token(MIN, '-')
            self.step()
            return self.current_token

        if self.current_char == '*':
            self.current_token = Token(MUL, '*')
            self.step()
            return self.current_token

        if self.current_char == '/':
            self.current_token = Token(DIV, '/')
            self.step()
            return self.current_token

        if self.current_char == '(':
            self.current_token = Token(LPAR, '(')
            self.step()
            return self.current_token

        if self.current_char == ')':
            self.current_token = Token(RPAR, ')')
            self.step()
            return self.current_token

        self.error()

class Interpreter():
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
        if self.current_token.type == INT:
            result = self.current_token.val
            self.eat(INT)
            return result
        elif self.current_token.type == LPAR:
            self.eat(LPAR)
            result = self.expr()
            self.eat(RPAR)
            return result

    def term(self):
        result = self.factor()

        while self.current_token.type in [MUL, DIV]:
            if self.current_token.val == '*':
                self.eat(MUL)
                result *= self.factor()
            elif self.current_token.val == '/':
                self.eat(DIV)
                result /= self.factor()
        
        return result

    def expr(self):
        result = self.term()

        while self.current_token.type in [SUM, MIN]:
            if self.current_token.val == '+':
                self.eat(SUM)
                result += self.term()
            elif self.current_token.val == '-':
                self.eat(MIN)
                result -= self.term()
        
        return result