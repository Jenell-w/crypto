from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    result = ""
    for char in text:
        char_idx = rotate_character(char, rot)
        result += char_idx      
    return result
    
