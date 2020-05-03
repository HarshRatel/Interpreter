import unittest
import interpreter as i


class InterpreterTests(unittest.TestCase):
    def _test_easy_term(self):
        expressions = {'-2+-2': -4,
                       '2*2': 4,
                       '123 * (1235 + 123)': 123 * (1235 + 123),
                       '44239 / 523': 44239 / 523}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.eval(), val)

    def _test_easy_expr(self):
        expressions = {'2+2': 4,
                       '1235 + 123': 1235 + 123,
                       '44239 - 523': 44239 - 523}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.eval(), val)

    def _test_complex_expr(self):
        expressions = {'2+2+543-123+(3145+123)-123124': 2+2+543-123+3145+123-123124,
                       '1235*123 + 123/532 * 123 / 75 -6456': 1235*123 + 123/532 * 123 / 75 - 6456,
                       '44239 - 523 -(12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)': 44239 - 523 - (12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)}

        for exp, val in expressions.items():
            intrepreter = i.Interpreter(exp)
            self.assertEqual(intrepreter.eval(), val)

    def test_program(self):
        code = 'BEGIN \
                    BEGIN \
                        number := 2; \
                        a := number; \
                        b := 10 * a + 10 * number / 4; \
                        c := a - - b \
                    END; \
                    x := 11; \
                END.'
        interpreter = i.Interpreter(code)
        print(interpreter.eval())


if __name__ == '__main__':
    unittest.main()
