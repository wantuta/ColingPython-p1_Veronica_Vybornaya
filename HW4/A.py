class SpaceObject:
    def __init__(self, name):
        self.name = name
        
class Planet(SpaceObject):
    def __init__(self, name, population):
        super().__init__(name=name)
        self.population = population or []
    def __str__(self):
        return f"На {self.name} живет {', '.join([animal.name for animal in self.population])}"

    
class Animal:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f" Животное {self.name}"
    def alive(self, planet):
        planet.population.append(self)

    
class Cat(Animal):
    def __init__(self, name, fur, color):
        super().__init__(name=name)
        self.fur = fur
        self.color = color

    def eating(self):
        print(f'{self.name} объелся вискасом')

        
class Jiraffe(Animal):
    def __init__(self, name, eyelashes, color, height, tiredness):
        super().__init__(name=name)
        self.eyelashes = eyelashes
        self.color = color
        self.height = height
        self.tiredness = 20
    def amusing_everyone(self):
        print(f'{self.name} испугал котов')
    def sleeping(self):
        print(f'{self.name} спит')
        self.tiredness -= 10

class Dog(Animal):
    def __init__(self, name, breed, color, height, training):
        super().__init__(name=name)
        self.breed = breed
        self.color = color
        self.height = height
        self.training = 0
    def amusing_everyone(self):
        print(f'{self.name} испугал котов')
    def educating_the_dog(self):
        print(f'{self.name} тренируется')
        self.training += 10

earth = Planet('Earth', population = [])

barsik = Cat(name='Барсик', fur = '', color = '')
barsik.alive(earth)
turbo = Dog(name='Турбо', breed = '', color = '', height = '', training = '')
turbo.alive(earth)
fluffy = Jiraffe(name='Дылда', eyelashes = '', color = '', height = '', tiredness = '')
fluffy.alive(earth)

print(earth)
