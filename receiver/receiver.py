from os import remove
from requests import get as geturl
from random import randint


async def receive_file_content(url):
    response = geturl(url)

    random_name = "file" + str(randint(1000, 10000)) + ".txt"
    if response.status_code == 200:
        with open(random_name, 'wb') as f:
            f.write(response.content)
            print('File downloaded successfully!')

        with open(random_name, 'r') as f:
            content = f.read()
        remove(random_name)
        return content
        # i have no idea why it could not work like the code bellow
        # return str(response.content)
    else:
        return 'err'
    
def receive_file_content_by_path(path):
    try:
        with open(path, 'r') as f:
            content = f.read()
        return content
    except:
        return "err"