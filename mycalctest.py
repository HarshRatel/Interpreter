import unittest
import mycalc as i

class InterpreterTests(unittest.TestCase):
    def test_token_parse(self):
        expressions = {'2+2' : 4,
                        '1235 + 123' : 1235 + 123,
                        '44239 - 523' : 44239 - 523}
        
        for exp, val in expressions.items():
            interpreter = i.Interpreter(exp)
            while interpreter.get_token().type is not i.EOF:
                print(interpreter.current_token)

    def test_easy_expr(self):
        expressions = {'2+2' : 4,
                        '1235 + 123' : 1235 + 123,
                        '44239 - 523' : 44239 - 523}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.expr(), val)

    def test_complex_expr(self):
        expressions = {'2+2+543-123+3145+123-123124' : 2+2+543-123+3145+123-123124,
                        '1235 + 123 - 123 + 123 - 123 -6456' : 1235 + 123 - 123 + 123 - 123 -6456,
                        '44239 - 523 -12523 + 1236 - 1235623' : 44239 - 523 -12523 + 1236 - 1235623}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.expr(), val)

if __name__ == '__main__':
    unittest.main()