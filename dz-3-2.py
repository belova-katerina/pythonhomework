def my_func(name, surname, birth, city, email, tel_number):
    print(f'name: {name}, surname: {surname}, birth: {birth}, city: {city}, email: {email}, phone number: {tel_number}')
my_func(name=input("Enter your name: "), surname=input("Enter your surname: "), birth=input("Enter your year of birth: "),
        city=input("Enter the city you live in: "), email=input("Enter your email: "), tel_number=input("Enter your phone number: "))