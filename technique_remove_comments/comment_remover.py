import re

def remove_comments(code):
    # Remove single-line comments
    code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
    
    # Remove multi-line comments
    # code = re.sub(r'"""[\s\S]*?"""', '', code)
    # code = re.sub(r"'''[\s\S]*?'''", '', code)
    
    return code


# comment

# //////////////// LOCAL TESTS

# sample_code = """#hi
# print(10)"""

# print(remove_comments(sample_code))