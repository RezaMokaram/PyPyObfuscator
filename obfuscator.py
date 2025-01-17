from technique_remove_comments.comment_remover import remove_comments
from technique_remove_spaces.empty_line_remover import remove_empty_lines
from technique_dead_line.adding_dead_lines import add_dead_lines
from technique_string_manupulation.string_manupulator import string_manupulator
from technique_variable_rename.variable_rename import variable_renamer

def obfuscate(code):
    obfuscated_code = code
    obfuscated_code = remove_comments(obfuscated_code)
    obfuscated_code = remove_empty_lines(obfuscated_code)
    obfuscated_code = add_dead_lines(obfuscated_code)
    obfuscated_code = string_manupulator(obfuscated_code)
    obfuscated_code = variable_renamer(obfuscated_code)
    return obfuscated_code