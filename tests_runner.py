# import sys
# sys.path.insert(1, '/home/reza/Documents/project')

from reciver.reciver import recive_file_content_by_path
from sender.sender import write_content_to_file
from obfuscator import obfuscate

tests_no = 5

for i in range(1, tests_no + 1):
    index = ""
    if i < 100:
        index += "0"
    if i < 10:
        index += "0"
    index += str(i)
    try:
        code = recive_file_content_by_path(f"./tests/test_{index}/code.py")
        obfuscated_code = obfuscate(code)
        write_content_to_file(obfuscated_code, f"./tests/test_{index}/resault.py")

    except:
        pass