def my_func(*args):

    try:
        arg1 = int(input("Введите делимое число: "))
        arg2 = int(input("Введите делитель: "))
        result = arg1 / arg2
    except ValueError:
        return 'Value error'
    except ZeroDivisionError:
        return 'Деление на ноль невозможно!'

    return result

print(f"Частное равно: {my_func()}")