

def myencode(data):
    key = 1
    mode = 1
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
               '1234567890*'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == 1 else index - key
            new_index %= len(alphabet)
            new_data += alphabet[new_index:new_index+1]
        return new_data

def mydecode(data):
    key = 1
    mode = 1
    alphabet = 'abcdefghijklmnopqrstuvwyzABCDEFGHIJKLMNOPQRSTUVWYZ' \
               'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
               '1234567890*()-=+/!@#:;'
    new_data = ''
    for c in data:
        index = alphabet.find(c)
        if index == -1:
            new_data += c
        else:
            new_index = index + key if mode == 1 else index - key
            new_index %= len(alphabet)
            new_data += alphabet[new_index:new_index+1]
        return new_data

