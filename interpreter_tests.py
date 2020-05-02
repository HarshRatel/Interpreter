import unittest
import interpreter as i

class InterpreterTests(unittest.TestCase):
    def test_easy_term(self):
        expressions = {'2*2' : 4,
                        '123 * (1235 + 123)' : 123 * (1235 + 123),
                        '44239 / 523' : 44239 / 523}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.eval(), val)

    def test_easy_expr(self):
        expressions = {'2+2' : 4,
                        '1235 + 123' : 1235 + 123,
                        '44239 - 523' : 44239 - 523}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.eval(), val)

    def test_complex_expr(self):
        expressions = {'2+2+543-123+(3145+123)-123124' : 2+2+543-123+3145+123-123124,
                        '1235*123 + 123/532 * 123 / 75 -6456' : 1235*123 + 123/532 * 123 / 75 -6456,
                        '44239 - 523 -(12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)' : 44239 - 523 -(12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.eval(), val)

if __name__ == '__main__':
    unittest.main()