polish_alphabet = ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "ń", "o", "ó", "p", "r", "s", "ś", "t", "u", "w", "y", "z", "ź", "ż"]
polish_alphabet_length = len(polish_alphabet)


def encode_character(char, key):

    if char not in polish_alphabet:
        return " "

    index = polish_alphabet.index(char)

    
    new_index = index + key
    if new_index >= polish_alphabet_length:
        new_index -= polish_alphabet_length
    
    return polish_alphabet[new_index]
    

def encode(original, key):
    temp = ""
    for char in original:
        temp+= encode_character(char, key)

    return temp

print(encode("Jakub Sternik", 5))



