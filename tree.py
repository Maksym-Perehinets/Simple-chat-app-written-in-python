beta = None
key = 1
while key == 1:
    print("Виберіть дію.", "Введіть 1 для підрахунку букв.", "Введіть 2 для сортування слів в алфавітному порядку.", sep='\n')
    beta = int(input("Виберіть дію "))
    a = input("Ведіть бажане слово або речення ")
    count = len(a)

    if beta == 1:

        letter = input("Enter character which you want to count ")
        print(letter, '=', a.count(letter))

    else:

        result = str(sorted(a.split(), key=str.lower))
        z = result.translate({ord(i): None for i in "[]''"})
        print(z.translate(({ord(i): '\n' for i in ","})))
