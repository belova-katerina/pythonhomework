class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def method_1(cls, day_month_year):
        date = []

        for el in day_month_year.split():
            if el != '-': date.append(el)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def method_2(day, month, year):
        if 0 < day < 32:
            print('все ок')
        else:
            print('Такого дня не существует')

        if 0 < month < 13:
            print('все ок')
        else:
            print('Такого месяца не существует')

        if 0 < year < 2021:
            print('все ок')
        else:
            print('Неправильно указан год')

    def __str__(self):
        return f'Дата: {Data.method_1(self.day_month_year)}'

today = Data(22-7-2020)
print(today)
#print(today.method_1(12, 12, 2000))
#print(today.method_2(33, 8, 2030))
#print(Data.method_2(12-12-2000))
#print(Data.method_1(33, 8, 2030))

