
# https://codereview.stackexchange.com/questions/182733/base-26-letters-and-base-10-using-recursion

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # or string.ascii_uppercase
N = len(ALPHABET)
ALPHABET_INDEX = {d: i for i, d in enumerate(ALPHABET, 1)}

def int_to_column_id(num):
    ''' Converts any positive integer to Base26(letters only) with no 0th 
    case. Useful for applications such as spreadsheet columns to determine which 
    Letterset goes with a positive integer.
    '''
    if num < 0:
        raise ValueError("Input should be a non-negative integer.")
    elif num == 0:
        return ""
    else:
        q, r = divmod(num - 1, N)
        return int_to_column_id(q) + ALPHABET[r]

def column_id_to_int(string):
    ''' Converts a string from Base26(letters only) with no 0th case to a positive
    integer. Useful for figuring out column numbers from letters so that they can
    be called from a list. Raises a ValueError unless every character is a letter.
    '''
    result = 0
    try:
        for char in string.upper():
            result = result * N + ALPHABET_INDEX[char]
        return result
    except KeyError:
        raise ValueError("Input string should only contain letters.")
        