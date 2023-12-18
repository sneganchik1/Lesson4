
#HW 10. задача 3
#Создайте пользовательскую функцию, принимающую произвольное количество аргументов и выводящую их затем на экран. Для вывода элементов полученного списка используйте цикл for. Вызовите функцию, передав ей в качестве значений целое число, вещественное число, строку и пустой список
# def funct (*lst):
#     for x in lst:
#         print(x)
# funct('2', '2.5', ('a', 'b', 'c'), [])



# HW 9. three_args
# Создайте функцию three_args(), которая принимает 1, 2 или 3 строго ключевых параметра.
#
# В результате ее работы на печать в консоль выводятся значения переданных переменных, но только если они не равны None.
#
# Получим, например, следующее сообщение: «Переданы аргументы: var1 = 2, var3 = 10».


#
# def three_args(var1 = None, var2 = None, var3 = None):
#     if (var1 != None and var2 != None and var3 != None):
#         print(f'Переданы аргументы: var1 = {var1}, var2 = {var2}, var3 = {var3}')
#     elif (var1 != None and var2 != None and var3 == None):
#         print(f'Переданы аргументы: var1 = {var1}, var2 = {var2}')
#     elif (var1 != None and var2 == None and var3 != None):
#         print(f'Переданы аргументы: var1 = {var1}, var3 = {var3}')
#     elif (var1 == None and var2 != None and var3 != None):
#         print(f'Переданы аргументы: var2 = {var2}, var3 = {var3}')
#     else:
#        print('Введите хотя бы 2 аргумента')
#
#
# three_args(var1 = 2, var2 = 'a', var3 = 10)


# HW 8. Sum_range
# Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения start
# до величины end включительно. Если пользователь задаст первое число большее чем второе,
# просто поменяйте их местами.


def sum_range():
    start = input('Введите первое число от 0 до 10: ')
    print(start)
    fin = input('Введите второе число от 0 до 10: ')
    print(fin)


    if start.isdigit() and int(start) > 0 < 10 and fin.isdigit() and int(fin) > 0 < 10:
        if start > fin:
            start, fin = fin, start
        sum1 = sum(range(int(start), int(fin) + 1))
        return sum1
    else:
        print('Вводить можно только целые положительные числа от 0 до 10')

result = sum_range()
print(result)
