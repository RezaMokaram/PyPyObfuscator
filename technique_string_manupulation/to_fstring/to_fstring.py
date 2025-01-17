import ast

class StringToFString(ast.NodeTransformer):
    def visit_Str(self, node):
        return ast.parse(f'f"{node.s}"').body[0].value

def convert_to_fstring(code):
    tree = ast.parse(code)
    transformer = StringToFString()
    new_tree = transformer.visit(tree)
    new_code = ast.unparse(new_tree)
    return new_code

# //////////////// LOCAL TESTS ////////////////////

# Example usage:
# code = '''
# ss = '{"44"[::-1]}'
# y = f'me'
# x = "hello"
# print("world")
# '''

# code = '''
# ss = "{'42'[::-1]}"
# print(ss)
# '''

# new_code = code
# # new_code = str(modify_strings_in_code(new_code))
# new_code = convert_to_fstring(new_code)
# print(new_code)