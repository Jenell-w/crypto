from helpers import alphabet_position, rotate_character

def encrypt(message, key):
    result = ""
    key_index = 0

    for char in message:
        rot_key = key[key_index]
        rot_amount = alphabet_position(rot_key)
        if char.isalpha():
            new_char = rotate_character(char, rot_amount)
            result += new_char
            key_index = (key_index + 1) % len(key)  
        else:
            result += char
    return result


