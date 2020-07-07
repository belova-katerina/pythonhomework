def my_sum():
    sum_result = 0
    ex = False
    while ex == False:
        number = input("Введите несколько чисел или нажмите Q, чтобы выйти: ").split()

        result = 0
        for el in range(len(number)):
            if number[el] == 'Q' or number[el] == 'q':
                ex = True
                break
            else:
                result = result + int(number[el])
        sum_result = sum_result + result
        print(f'Текущая сумма равна: {sum_result}')
    print(f'Итоговая сумма равна: {sum_result}')

my_sum()