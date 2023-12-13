import string
import random
import secrets

def generate_password(length=10,symbols=True,uppercase=True):
    digits = string.digits
    lower = string.ascii_lowercase 
    chars = digits + lower

    if uppercase:
        chars = chars + string.ascii_uppercase
    if symbols:
        chars = chars + string.punctuation

    chars_length = len(chars)
    passwd = ''

    for i in range(length):
        # passwd = passwd + random.choice(chars)
        passwd = passwd + chars[secrets.randbelow(chars_length)]
    
    return passwd

def contains_upper(word):
    result = False
    for i in word:
        if i in string.ascii_uppercase:
            result = True
            break
    return result

def contains_symbols(word):
    result = False
    for i in word:
        if i in string.punctuation:
            result = True
            break
    return result

if __name__ == "__main__":
    for i in range(1,6):
        newpass = generate_password(length=12,symbols=True,uppercase=True)
        print(f'{i} --- {newpass} (U: {contains_upper(newpass)}, S: {contains_symbols(newpass)})')