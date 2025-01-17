# def remove_empty_lines(code):
#     lines = code.split("\n")
#     non_empty_lines = [line for line in lines if line.strip()]
#     cleaned_code = "\n".join(non_empty_lines)
#     return cleaned_code

def remove_empty_lines(code):
    lines = code.split("\n")
    non_empty_lines = [line for line in lines if line.strip() != ""]
    return "\n".join(non_empty_lines)

# /////////// LOCAL TEST

# sample_code = """a=int(10)

# print(a)
# """

# print(remove_empty_lines(sample_code))