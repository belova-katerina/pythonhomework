from sys import  argv
hours, rate, bonus = map(float, argv[1:])
try:
    print(hours * rate + bonus)
except ValueError:
    print('not a number, try again')
