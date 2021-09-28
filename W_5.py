z =7
print('if you want add num enter 1',
             'substarction enter 2 ',
             'multiplying enter 3',
             'division enter 4 ', sep ='\n')

def add(a, b ):
    print(a+b)

def sub(a, b):
    print(a-b)
                        #Функції математичних дій
def mult(a, b):
    print(a*b)

def div(a, b):
    if b > 0:
        print(a/b)
    else:
        print('eror')

add(4,5)
while z == 7:
    oper = int(input('enter hire '))
    num1 = float(input('enter your number'))
    num2 = float(input('enter your number'))
    if oper == 1:
        add(num1,num2)
    elif oper == 2:
        sub(num1, num2)
    elif oper == 3:
       mult(num1,num2)
    elif oper == 4:
        div(num1,num2 )
    z = input('To exit enter any namber') or  7
else:
    print('thx for using code')


