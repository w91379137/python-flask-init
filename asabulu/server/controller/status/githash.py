
'''
https://janakiev.com/blog/python-shell-commands/
'''

import os

def githash():

    result = ''
    try:
        stream = os.popen('git rev-parse --short HEAD')
        result = stream.read()
    except Exception as e:
        print(f"Error:{e}")
        # raise e
    
    return result
