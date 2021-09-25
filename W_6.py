messange=str(input())

def pal():
    global messange
    new_messange=""
    for i in messange[::-1]:
        new_messange += i                       #функція що оприділяє чи є слово полідормом
    if messange == new_messange:
        print('palindrom')

    else:
        print("not a palindrom")


pal()