import re


def name_generator(steper):
    return "HEXx" + str(steper)


def variable_renamer(code):
    steper = 799645531
    # add \n so regex picks it up
    code = "\n" + code
    variable_names = re.findall(r"(\w+)(?=( |)=( |))", code)
    for i in range(len(variable_names)):
        steper += 1
        # if steper == 1000000000: 
        #     steper = 1
        obfuscated_name = name_generator(steper=steper)
        code = re.sub(
            r"(?<=[^.])(\b{}\b)".format(variable_names[i][0]), obfuscated_name, code
        )
    return code

# ///////// LOCAL TEST

# sample_code = """def aaa():pass
# a="hello"
# aa="bd"
# b=" world!"
# print(a+b)"""

# print(variable_renamer(sample_code))