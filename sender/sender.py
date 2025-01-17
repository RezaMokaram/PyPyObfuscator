import os

from typing import Final

file_path = os.path.dirname(os.path.abspath(__file__))
CLI_OUTPUT_PATH : Final = os.path.join(file_path, "..", "cli_output", "cli_obfuscated_code.py")

def write_content_to_file(content, path = CLI_OUTPUT_PATH):
    print(path)
    try:
        with open(path, 'w') as f:
            f.write(content)
        return "ok"
    except Exception as e:
        print(e)
        return "err"