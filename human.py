'''
Task:
1) make test of 1 method from class Human..there is example of the code from src/some_module.py in test/test_some_module.py
=> on the left panel there is icon of glass for chemistry testing, there are tests also visible
=> in terminal it can be run for example just with command pytest because pytest is installed in python pipenv virtual environment
=> read how to make test, especially pytest for a class method
=> also there is some convention structure of the project folders => code in python files is 
in folder src and tests in folder test or tests
=> there is possible to use file conftest

2) make new module employee.py, where will be class Employee, which will be inherited from class Human
and there will be one yet empty specified method for class Employee (the other are the same as in Human class
and doesn't need to be specified, if they don't change..they are inherited from Human..you can try to test some..)
'''

class Human():
    type_of_animal = 'original'  # this is class variable
    def __init__(self, age, sex, first_name, last_name, lenght_in_cm, hair_colour):
        self.age = age
        self.sex = sex
        self.first_name = first_name
        self.last_name = last_name
        self.length = lenght_in_cm
        self.hair_colour = hair_colour
        self.phone_number = None
        self.address = None

    def get_hair_colour(self):
        hair_colour_to_be_returned = self.hair_colour
        return hair_colour_to_be_returned

    def get_full_name(self):
        full_name = self.first_name + ' ' + self.last_name
        return full_name

    def _age_in_days(self): # when method is used only in class and it is not used publicly (outside of the class), it starts with _
        return 365 * self.age

    def get_age_in_days(self):
        return self._age_in_days()

    def get_details(self):
        return f'{self.type_of_animal} {self.get_full_name()}'

    def phone_adress(self, human_number, human_adress):
        self.phone_number = human_number
        self.address = human_adress

    def get_phone_adress(self):
        return f'The adress of {self.get_full_name()} is {self.address} and phone number is {self.phone_number}'

if __name__ == "__main__":
    human_1 = Human(6, 'man', 'Stepan', 'Rozum', 120, 'brown')
    human_2 = Human(4, 'woman', 'Naomi', 'Rozumova', 100, 'blond')
