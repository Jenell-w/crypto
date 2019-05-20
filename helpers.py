def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if letter.isupper():
        letter = letter.lower()
        
    result = alphabet.index(letter)    
    return result 

def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    for letters in char:
        if char not in alphabet:
            if char not in alphabet2:
                return char
        rot_ind = (alphabet_position(char) + rot) % 26
        if letters in alphabet2:
            result += alphabet2[rot_ind]
            result.upper()
            continue
        else:
            result += alphabet[rot_ind]       
    return result   
