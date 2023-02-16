def some_function(name, surname):
    return f'Hello, {name} {surname}.'

class Animal():
    sounds_of_animals = {'frog': 'kvak', 'dog': 'whooof', 'cat': 'miau'}
    def __init__(self, animal_type):
        self.type = animal_type

    @property
    def sound(self):
        get_sound = self.sounds_of_animals.get(self.type)
        if not get_sound:
            return 'unknown sound'
        else:
            return get_sound

if __name__ == '__main__':
    frogie_bikaboc = Animal('frog')
    print(frogie_bikaboc.sound)
