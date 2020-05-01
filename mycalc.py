INT, EOF, SUM, MIN = 'INT', 'EOF', 'SUM', 'MIN'

class Token():
    def __init__(self, token_type, val = None):
        self.type = token_type
        self.val =  val

    def __str__(self):
        return "Token ({}, {})".format(self.type, self.val)

    def __repr__(self):
        return self.__str__()

class Interpreter():
    def __init__(self, code : str):
        self.code = "".join([s for s in code if s != ' '])
        self.pos = 0
        self.current_char = self.code[self.pos]
        self.current_token = None

    def error(self):
        raise Exception("Failed parse input")

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

        return digit

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

    def expr(self):
        while self.get_token().type is not EOF:
            print(self.current_token)