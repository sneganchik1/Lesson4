from libr.factorial import factorial
import datetime

"""
ищем время выполнения посчета факториала через декоратор
"""
def time_func(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        print(f'start time  {start_time}')
        res = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f'end time  {end_time}')

        delta = end_time - start_time
        print(f' время выполнения расчетов {delta}')
        return res

    return wrapper

@time_func
def fact_dec(n):
    return factorial(n)

# print(factorial(5))
print(fact_dec(50))


