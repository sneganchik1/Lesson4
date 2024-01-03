
# HW 13. Калькулятор
# Напишіть функцію, яка отримує 3 аргументи: перші 2 - числа, третій -
# операція (+, -, *, /), яка повинна бути проведена над ними.
# У випадку невідомої операції, функція повертає рядок Unknown
# operation. Результатом має бути дійсне число з двома знаками
# після десяткової крапки.

"""
создание простейшего калькулятора + - / *
"""

x = int(input('Type a number 0-10: '))
y = int(input('Type a number 1-10: '))
s = input('Type one of those symbols :  + , - , * , /      :')
def calculator(x, y, s):

    if (0 <= x <= 10) and (1 <= y <= 10) and (s in {"*", "/", "+", "-"}):   #вместо (s == "*" or "/" or "+" or "-"):
        if s == "+":
            res = x + y
        elif s == "-" :
            res = x - y
        elif s == "*" :
            res = x * y
        elif s == "/" and y != 0 :
            res = x / y
        elif s == "/" and y == 0 :
            print("на 0 делить нельзя")
            return None
        else:
            print ("Smth goes wrong - Unknown operation")
            return None

        return res

    else:
        print("Smth goes wrong - Unknown operation")
        return None


result = calculator(x, y, s)

if result != None:
    print(round(result, 2))



