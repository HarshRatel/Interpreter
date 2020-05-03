import unittest
from lexer import Lexer
from astree import OpNode, NumNode
from token_types import *
def print_tree(node):
    if isinstance(node, NumNode):
        print("numnode {}".format(node.val))
    elif isinstance(node, OpNode):
        print('opnode {}'.format(node.val))
        print_tree(node.left)
        print_tree(node.right)
    
class ParserTests(unittest.TestCase):
    def test_complex_expr(self):
        expressions =   {   
                            'BEGIN END.' : 6,
                            'BEGIN a := 5; x := 11 END.' : 8,
                            'BEGIN a := 5; x := 11; END.' : 2+2+543-123+3145+123-123124,
                            'BEGIN BEGIN a := 5 END; x := 11 END.' : 1235*123 + 123/532 * 123 / 75 -6456,
                        }

        for exp, val in expressions.items():
            print(exp + '\n')
            lexer= Lexer(exp)
            token = lexer.get_token()
            print(token)
            while token.type != EOF:
                token = lexer.get_token()
                print(token)
            
if __name__ == '__main__':
    unittest.main()