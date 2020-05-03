import unittest
from tokens_parser import Parser
from astree import OpNode, NumNode, Compound, Assign, Var


def print_tree(node):
    res = ''
    if isinstance(node, Compound):
        for child in node.children:
            res += print_tree(child)
    if isinstance(node, Var):
        res += 'var {}'.format(node.var)
    elif isinstance(node, Assign):
        res += 'assign {} := {}'.format(node.left.var,
                                        print_tree(node.right))
    elif isinstance(node, NumNode):
        res += "numnode {}".format(node.val)
    elif isinstance(node, OpNode):
        res += 'opnode {}'.format(node.val)
        res += print_tree(node.left)
        res += print_tree(node.right)

    return res + '\n'


class ParserTests(unittest.TestCase):
    def _test_complex_expr(self):
        expressions = {'2+2 + 2': 6,
                       '(2+2)*2': 8,
                       '2+2+543-123+(3145+123)-123124': 2+2+543-123+3145+123-123124,
                       '1235*123 + 123/532 * 123 / 75 -6456': 1235*123 + 123/532 * 123 / 75 - 6456,
                       '44239 - 523 -(12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)': 44239 - 523 - (12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)}

        for exp, val in expressions.items():
            print(exp + '\n')
            tree = Parser(exp).parse()
            print_tree(tree)
            print()

    def test_code(self):
        code = 'BEGIN \
                    BEGIN \
                        number := 2; \
                        a := number; \
                        b := 10 * a + 10 * number / 4; \
                        c := a - - b \
                    END; \
                    x := 11; \
                END.'
        print(code)
        tree = Parser(code).parse()
        print(print_tree(tree))


if __name__ == '__main__':
    unittest.main()
