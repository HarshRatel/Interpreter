import unittest
from tokens_parser import Parser
from astree import OpNode, NumNode

def print_tree(node):
    if isinstance(node, NumNode):
        print("numnode {}".format(node.val))
    elif isinstance(node, OpNode):
        print('opnode {}'.format(node.val))
        print_tree(node.left)
        print_tree(node.right)
    
class ParserTests(unittest.TestCase):
    def test_complex_expr(self):
        expressions = { '2+2 + 2' : 6,
                        '(2+2)*2' : 8,
                        '2+2+543-123+(3145+123)-123124' : 2+2+543-123+3145+123-123124,
                        '1235*123 + 123/532 * 123 / 75 -6456' : 1235*123 + 123/532 * 123 / 75 -6456,
                        '44239 - 523 -(12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)' : 44239 - 523 -(12523 + (1236 - 1235623) * 1312) / 123 + (2134 / 123)}

        for exp, val in expressions.items():
            print(exp + '\n')
            tree= Parser(exp).parse()
            print_tree(tree)
            print()
            
if __name__ == '__main__':
    unittest.main()