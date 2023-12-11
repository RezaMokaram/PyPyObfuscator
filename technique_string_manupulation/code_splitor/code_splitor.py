import ast
from random import randint

def reverse_string(input_string):
    return input_string[::-1]

def split_string_randomly(input_string, num_parts):
    parts = []
    if len(input_string) <= num_parts:
        num_parts = 1
    part_len = int(len(input_string) / num_parts)
    iterator = 0

    for i in range(0, num_parts - 1):
        parts.append("")
        last_index = len(parts) - 1
        for j in range(0, part_len): 
            parts[last_index] = ''.join([parts[last_index], str(input_string[iterator])])
            iterator += 1

    parts.append("")
    last_index = len(parts) - 1
    for j in range(iterator, len(input_string)): 
        parts[last_index] = ''.join([parts[last_index], str(input_string[j])])

    return parts

def manipulate_string(s):
    answer = ""
    res = split_string_randomly(s, randint(1,5))

    for i in range(0, len(res)):
        res[i] = reverse_string(res[i])
        answer = ''.join([answer , "{str(\'" , str(res[i]) , "\'[::-1])}"])

    return answer

def modify_strings_in_code(code):
    class StringModifier(ast.NodeTransformer):
        def visit_Str(self, node):
            new_s = manipulate_string(node.s)
            return ast.Str(s=new_s)

    tree = ast.parse(code)

    StringModifier().visit(tree)

    modified_code = ast.unparse(tree)

    return modified_code


# ///////////// LOCAL TESTS //////////////////////
# code = """
# mystr = "HELLO WORLD!"
# print(mystr)
# """

# print(modify_strings_in_code(code))
# book = "hi bro masht nalkfdn s,kfndwl "
# print(split_string_randomly(book, 4))