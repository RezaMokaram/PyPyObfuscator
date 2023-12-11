import sys
import os

current_directory = os.getcwd()

# print(current_directory)
#                   /home/reza/Documents/project/technique_string_manupulation
sys.path.insert(1, f'{current_directory}/technique_string_manupulation')

from code_splitor.code_splitor import modify_strings_in_code
from to_fstring.to_fstring import convert_to_fstring

def string_manupulator(code):
    try:
        res = code
        res = modify_strings_in_code(res)
        res = convert_to_fstring(res)
        return res
    except:
        return code
    
# //////////////// LOCAL TESTS 

# code = '''
# ss = "hello world! programmer python reverse computer engineering !!!"
# print(ss)
# '''

# print(string_manupulator(code))

# //////////////// LOCAL TESTS OUTPUT

# ss = f"{str(' redorb olleh'[::-1])}{str('yp  remargorp'[::-1])}{str('retupmoc noht'[::-1])}{str('!!! gnireenigne '[::-1])}"
# print(ss)