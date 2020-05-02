from lexer_tokens import Token
from token_types import INT, EOF, SUM, MIN, DIV, MUL, LPAR, RPAR

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