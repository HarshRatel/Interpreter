# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MUL', 'DIV', 'EOF'


class Token(object):
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: 0, 1, 2. 3, 4, 5, 6, 7, 8, 9, '+', or None
        self.value = value

    def __str__(self):
        """String representation of the class instance.

        Examples:
            Token(INTEGER, 3)
            Token(PLUS '+')
        """
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()


class Interpreter(object):
    def __init__(self, text):
        # client string input, e.g. "3+5"
        self.text = "".join([s for s in text if not s.isspace()])

        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')
    
    def step(self):
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None
            
    def get_next_token(self):
        """Lexical analyzer (also known as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        """
        text = self.text

        # is self.pos index past the end of the self.text ?
        # if so, then return EOF token because there is no more
        # input left to convert into tokens
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        # get a character at the position self.pos and decide
        # what token to create based on the single character
        self.current_char

        # if the character is a digit then convert it to
        # integer, create an INTEGER token, increment self.pos
        # index to point to the next character after the digit,
        # and return the INTEGER token
        if self.current_char.isdigit():
            digit = ''
            while self.current_char is not None and self.current_char.isdigit():
                digit += self.current_char
                self.step()

            return Token(INTEGER, int(digit))

        if self.current_char == '-':
            token = Token(MINUS, self.current_char)
            self.step()
            return token

        if self.current_char == '+':
            token = Token(PLUS, self.current_char)
            self.step()
            return token

        if self.current_char == '*':
            token = Token(MUL, self.current_char)
            self.step()
            return token

        if self.current_char == '/':
            token = Token(DIV, self.current_char)
            self.step()
            return token

        self.error()

    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """expr -> INTEGER PLUS INTEGER"""
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()
        
        # we expect the current token to be a single-digit integer

        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        if op.type is PLUS:
            self.eat(PLUS)
        elif op.type is MINUS:
            self.eat(MINUS)
        elif op.type is MUL:
            self.eat(MUL)
        elif op.type is DIV:
            self.eat(DIV)

        right = self.current_token
        self.eat(INTEGER)
        self.eat(EOF)

        if op.type is PLUS:
            result = left.value + right.value
        elif op.type is MINUS:
            result = left.value - right.value
        elif op.type is MUL:
            result = left.value * right.value
        elif op.type is DIV:
            result = left.value / right.value

        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()