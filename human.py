'''
Task:
1) make test of 1 method from class Human
=> read how to make test, especially pytest for a class method
=> also there is some convention structure of the project folders => code in python files is 
in folder src and tests in folder test or tests
=> there is possible to use file conftest
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
'''
This is test for commit change in comment
hair_colour_of_human_1 = human_1.get_hair_colour()
hair_colour_of_human_2 = human_2.get_hair_colour()
hair_colour_of_human_1_another_way = human_1.hair_colour
print(hair_colour_of_human_1)
print(hair_colour_of_human_1_another_way)
print(hair_colour_of_human_2)
print('Lenght of human_1:', human_1.length, ' centimeters')
print('Lenght of human_2:', human_2.length, ' centimeters')
length_of_stopik_plus_naomi = human_1.length + human_2.length
print('Stopik + Naomi length is:', length_of_stopik_plus_naomi, ' centimeters')
print('Specific human first name:', human_1.first_name)
print('Specific human last name:', human_1.last_name)
print('Specific human full name:', human_1.get_full_name())
human_1.first_name = 'Stopinek'
print('Changed first name of human_1:', human_1.first_name)
print('Specific human full name after change:', human_1.get_full_name())
print(f'Print age of {human_1.get_full_name()} is {human_1.get_age_in_days()}')
print(f'Print age of {human_2.get_full_name()} is {human_2.get_age_in_days()}')
print(human_1.type_of_animal)
print(human_2.type_of_animal)
Human.type_of_animal = 'tiger'
print(human_1.type_of_animal)
print(human_2.type_of_animal)
print(human_1.get_details())
print(human_2.get_details())
print(human_1.type_of_animal)
human_1.type_of_animal = 'human'
print(human_1.type_of_animal)
print(human_2.type_of_animal)
print(Human.type_of_animal)
Human.type_of_animal = 'original'
print(human_1.type_of_animal)
print(human_2.type_of_animal)
print(Human.type_of_animal)


human_1.phone_adress('7774568', 'Manetinska 43')
print(human_1.get_phone_adress())

'''