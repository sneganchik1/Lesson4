
# HW 14. Пори року
# Напишіть функцію, яка повертає назву пори року для введеного значення
#
# номера місяця. У випадку некоректного номеру функція повертає
#
# замість пори року `unknown`
#
# (12 -> winter, 5 -> summer , 15 -> 'unknown' ... )

"""
проверяем введенное число на принадлежность к условиям
"""

def month_check():
    month = int(input('Введите номер месяца : '))
    print(month)

    if (month == 12 or month == 1 or month == 2) :
        print(' Пора року цього місяця - winter')
    elif 3 <= month <= 5:
        print(' Пора року цього місяця - spring')
    elif 6 <= month <= 8:
        print(' Пора року цього місяця - summer')
    elif 9 <= month <= 11:
        print(' Пора року цього місяця - autumn')
    else:
        print('unknown')


month_check()
