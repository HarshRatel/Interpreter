import unittest
import mycalc as i

class InterpreterTests(unittest.TestCase):
    def test_token_parse(self):
        expressions = {'2+2' : 4,
                        '1235 + 123' : 1235 + 123,
                        '44239 - 523' : 44239 - 523}

        for exp, val in expressions.items():
            interpreter = i.Interpreter(exp)
            #self.assertEqual(interpreter.expr(), val)
            interpreter.expr()

if __name__ == '__main__':
    unittest.main()