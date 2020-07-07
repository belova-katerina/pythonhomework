def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif b < a < c:
        return a + c
    else:
        return b + c

print(f"Результат - {my_func(int(input('Введите первый аргумент: ')), int(input('Введите второй аргумент: ')), int(input('Введите третий аргумент: ')))}")