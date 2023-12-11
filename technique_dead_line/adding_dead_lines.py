from random import randint


dead_line_code = [
    ["X = 7**3", "Y = 4", "Y += X"],
    ["X = 'password: secretpassword1234'[::-1]", "Y = 'username: rezamokaram ' + X"]
]

indentation_increasers = ["for", "if", "switch", "case", "while", "def", "elif", "else", "with", "try", "except", "class", "async"]

def name_generator(steper):
    return "VARx" + str(steper)

def add_dead_lines(code):
    steper = 568954954
    resault_code = ""
    lines = code.split("\n")
    indent = ""
    total_added_lines = 40

    for line in lines:
        rstrp_line = line.rstrip()
        resault_code += rstrp_line + "\n"
        indent = ""
        
        # def if for while switch case
        striped_line = line.strip()
        striped_line = striped_line.replace('(', ' ')
        striped_line = striped_line.replace(':', ' ')
        words = striped_line.split(' ')
        first_word = ""
        if len(words) >= 1:
            first_word = words[0]
        if first_word in indentation_increasers:
            # continue
            indent = "    "
        
        # setting the indent
        for i in range(0, len(rstrp_line)):
            if line[i] == ' ':
                indent += ' '
            else:
                break
        
        # block to add dead lines
        flag = randint(0, 2)
        if total_added_lines <= 0 or flag%2==1:
            continue

        random_index = randint(0, len(dead_line_code)-1)
        # print (f"------> {len(dead_line_code)}\n\n")
        codes = dead_line_code[random_index]

        variable_X = name_generator(steper)
        steper += 1
        variable_Y = name_generator(steper)
        steper += 1
        
        for chunk_code in codes:
            # print(chunk_code)
            new_line = chunk_code
            new_line = new_line.replace('X', variable_X)
            new_line = new_line.replace('Y', variable_Y)
            resault_code += indent + new_line + "\n"
            
    return resault_code

# ///////////// LOCAL TESTS

# sample_code = """
# def sayhi():
#     print(y)
#     print(y)

    
# mstr = "Hello World!"
# print(mstr)
# x = int(6)
# x += 7
# print(x)
# """

# print(add_dead_lines(sample_code))