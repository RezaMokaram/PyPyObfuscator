import ast

def name_generator(steper):
    return "HHHx" + str(steper)

# def is_usable_character(char):
#     if(char >= 'a' and char <= 'z'):
#         return True
#     if(char >= 'A' and char <= 'Z'):
#         return True
#     if(char >= '0' and char <= '9'):
#         return True
#     if(char == '.' or char == '_'):
#         return True
#     return False



def get_function_names(code):
    # Parse the code into an abstract syntax tree (AST)
    tree = ast.parse(code)
    
    # Initialize an empty list to store the function names
    function_names = []
    
    # Iterate over each node in the AST
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Add the name of the function to the list
            function_names.append(node.name)
    
    return function_names

def change_function_names(code):
    function_names = get_function_names(code)
    lines = code.split('\n')
    steper = 697865412
    # Iterate over each line and replace the function names
    for i, line in enumerate(lines):
        for old_name in function_names:
            if old_name in line:
                # Replace the old function name with the new function name
                new_name = name_generator(steper)
                steper += 1
                lines[i] = line.replace(old_name, new_name)
    
    # Join the modified lines back into a single string
    modified_code = '\n'.join(lines)
    
    return modified_code

# ////////////////// LOCAL TEST
# sample_code = '''
# def function1():
#     pass

# def function2():
#     pass

# def function3():
#     pass

# '''

# print(change_function_names(sample_code))
