import os

from reciver.reciver import recive_file_content_by_path as code_reader
from sender.sender import write_content_to_file
from obfuscator import obfuscate
#    /home/reza/Documents/acm/python/my.py

if __name__ == '__main__':
    while(1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("///////////////////////")
        print("Please choose a number")
        print("0. Exit")
        print("1. Obfuscate by path")
        print("///////////////////////")
        choice = input()
        if choice == '1':
            
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Please Enter your path to the file:")
            path = input()
            plain_code = code_reader(path)
           
            if plain_code == 'err':
                print("An error ocurred while opening the file!")
            else:
                obfuscated_code = obfuscate(plain_code)
                result = write_content_to_file(obfuscated_code)
                if result == 'err':
                    print("An error ocurred while writing code to the destination file!")
                else:
                    print("Code successfully obfuscated!")
                    
            input("Press enter key to continue...")
        elif choice == '0':
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            pass