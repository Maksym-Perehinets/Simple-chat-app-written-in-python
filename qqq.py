alfavit_EN = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890*/'
alfavit_UA = 'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ1234567890*()/'
krok = int(1)
while True:
    shifr = input("Виберіть шифр фбо дешфр")
    message = input("Повідомлення для шифрування: ").upper()
    itog = ''
    lang = input('Виберіть мову UA/EN: ')

    if shifr == "шифр":
        if lang == 'UA':
            for i in message:
                mesto = alfavit_UA.find(i)
                new_mesto = mesto + krok
                if i in alfavit_UA:
                    itog += alfavit_UA[new_mesto]
                else:
                    itog += i
        else:
            for i in message:
                mesto = alfavit_EN.find(i)
                new_mesto = mesto + krok
                if i in alfavit_EN:
                    itog += alfavit_EN[new_mesto]
                else:
                    itog += i

    elif shifr == "дешифр":

        if lang == 'UA':
            for i in message:
                mesto = alfavit_UA.find(i)
                new_mesto = mesto - krok
                if i in alfavit_UA:
                    itog += alfavit_UA[new_mesto]
                else:
                    itog += i

        else:
            for i in message:
                mesto = alfavit_EN.find(i)
                new_mesto = mesto - krok
                if i in alfavit_EN:
                    itog += alfavit_EN[new_mesto]
                else:
                    itog += i

    print(itog)