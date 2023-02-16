'''
In this module are examples of the tests of the methods,
one method some_function in module some_module.py not in a class,
one other method sound is inside a class Animal..

=> tests must in best test all the main functionalities in the code..
'''
from src import some_module

def test_some_function():
    name = "Anna"
    surname = "Rozumova"
    assert some_module.some_function(name, surname) == 'Hello, Anna Rozumova.'


def test_get_known_sound():
    # here it tests sound of the known animal
    test_animal = 'frog'
    expected_sound = 'kvak'
    assert some_module.Animal(test_animal).sound == expected_sound


def test_get_unknown_sound():
    # here it tests sound of the unknown animal
    test_animal = 'megaduck'
    expected_sound = 'unknown sound'
    some_specific_one = some_module.Animal(test_animal)  # compare previous test with frog, this is also possible
    assert some_specific_one.sound == expected_sound
