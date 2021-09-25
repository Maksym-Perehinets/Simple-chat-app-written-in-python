alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZЯ' \
          'АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ' \
          '1234567890*/'
krok = int(1)
while True:
    shifr = input("Виберіть шифр фбо дешфр")
    message = input("Повідомлення для шифрування: ").upper()
    itog = ''

    if shifr == "шифр":

        for i in message:
            mesto = alfavit.find(i)
            new_mesto = mesto + krok
            if i in alfavit:                 #шифруєм укр символи за допомогою зміщення на 1 вперід змінна krok
                itog += alfavit[new_mesto]
            else:
                    itog += i

    else:

        for i in message:
            mesto = alfavit.find(i)
            new_mesto = mesto - krok
            if i in alfavit:
                itog += alfavit[new_mesto]           #дешифруємо за дпомогою зміщення на 1 назад змінна krok
            else:
                    itog += i

    print(itog.lower())


