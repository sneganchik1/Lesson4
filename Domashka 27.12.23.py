import factorial
import datetime

"""
ищем время выполнения посчета факториала через декоратор
"""
def time_func(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        delta = end_time - start_time
        print(f' время выполнения расчетов {delta}')
        return result

    return wrapper

@time_func
def find_fact(n):
    return factorial.factorial(n)

result = find_fact(5)
print(f'результат факториала составляет {result}')


