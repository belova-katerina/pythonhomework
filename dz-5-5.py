def summary():
    try:
        with open('file_task5.txt', 'w+', encoding='utf-8') as file_obj:
            line = input('Введите цифры через пробел: \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле!')
    except ValueError:
        print('Некорректное число. Ошибка ввода-вывода!')
summary()