class MyError (Exception):
    def __init__(self, text):
        self.text = text

    def my_error():
        dividend = int(input('Введите делимое: '))
        divisor = int(input('Введите делитель: '))

        try:
            if divisor == 0:
                raise MyError('Вы чего? Деление на ноль невозможно!')
            result = dividend / divisor
        except MyError as err:
            print(err)
        else:
            print(f'Все ок, результат деления: {result}')
        finally:
            print('Программа завершена, адьос!')

my_error()

# Мария, сделала как вы подсказали, но все равно выдает ошибку в 20 строке, что my_error not defined
# не понимаю, я ведь обозначила my_error в 5 строке, чего он ругается?((