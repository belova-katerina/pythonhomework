class Machines:
    def __init__(self, name, price, quantity, pages, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.pages = pages
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Name' : self.name, 'price' : self.price, 'quantity' : self.quantity}

    def __str__(self):
        return  f'{self.name}, price {self.price}, quantity {self.quantity}'

    def reception(self):
        try:
            unit = input('Enter the name of machine: ')
            unit_price = int(input('Enter the price for 1 piece: '))
            unit_quantity = int(input('Enter the quantity: '))
            unique = {'Name' : unit, 'price' : unit_price, 'quantity' : unit_quantity}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Current store list:\n {self.my_store}')
        except:
            return f'Input error!'

        print(f'Press Q to exit, press Enter to continue')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return Machines.reception(self)

class Printer(Machines):
    def to_print(self):
        return f'to print a document {self.pages} times'

class Scanner(Machines):
    def to_scan(self):
        return f'to scan a document {self.pages} times'

class CopyMachine(Machines):
    def to_copy(self):
        return f'to copy a document {self.pages} times'


unit_1 = Printer('HP 520', 5000, 150, 4)
unit_2 = Scanner('HP 780', 3500, 18, 7)
unit_3 = CopyMachine('Canon 123', 4800, 78, 18)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copy())