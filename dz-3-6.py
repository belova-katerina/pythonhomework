def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()


def int_func(text):
    words = input("Input words ")
    words = text.split()
    result = []
    for i in text:
        if i.isupper() == True:
            return "Введите буквы в нижнем регистре"

        if ord(i) > 122 or ord(i) < 97:
            print('Ошибка! Введите латинские буквы!')

    new_word = word.title()
    result.append(new_word)
    return ''.join(result)

