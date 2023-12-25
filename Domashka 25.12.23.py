# ДЗ 11. Скільуи разів певна літера зустрічаеться у строці
# Программа приймає на вхід будь яку строку (до 100 символів) і символ кількість входження якого треба порахувати.
#
# Приклад:
#
# строка - "hello world"
#
# літера - l
#
# Результат: 3
#
# Написати функцію з використанням рекурсії




def count_l(input_string):
    repeats = {}
    for char in input_string:
        if char in repeats:
            repeats[char] += 1
        else:
            repeats[char] = 1
    return repeats



def count_recurs(input_string, symbol_count):
    count_symbol = input_string.count(symbol_count)

    if count_symbol > 0:
        print(f"Літера '{symbol_count}' повторюється {count_symbol} разів")
        return #True

    else:
        print(f"Літера '{symbol_count}' не знайдена. Спробуйте іншу.")
        new_symbol_count = input("Введіть нову літеру :")
        count_recurs(input_string, new_symbol_count)


string_input = input('Введіть строку на 20 символів: ')

result = count_l(string_input)

print("Ви ввели строку:", string_input)
print("Символи повторюються :", result)

symbol_count = input('Введіть літеру : ')

count_recurs(string_input, symbol_count)


