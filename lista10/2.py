words = sorted([word.strip() for word in open("popularne_slowa2023.txt", 'r', encoding='utf8')], key=len)
words_grouped = {}

for word in words:
    if len(word) in words_grouped.keys():
        words_grouped[len(word)].add(word)
    else:
        words_grouped.update({len(word): set(word)})


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

length_keys = sorted(words_grouped.keys())
print(length_keys)
max_cesar = ""
max_cesar_length = 0

for key in length_keys:
    print(key, "---------------")
    if max_cesar_length > key:
        continue
    for word in words_grouped[key]:
        for i in range(1,31):
            if encode(word, i) in words_grouped[key] and len(word) >= max_cesar_length:
                max_cesar = word
                max_cesar_length = len(max_cesar)
                print(max_cesar)
                break









