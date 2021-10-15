# All the Code Written By Asif date 27th September 2021
# Objects and Class

# Animal is-a object (yes, sort of confusing) look at the extra
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## self.name has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):
    
    def __init__(self, name):
        ## self.name has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## self.name has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Employee has-a name
        super(Employee, self).__init__(name)
        # self.salary has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salman is-a Fish
class Salman(Fish):
    pass

# Halbut is-a Fish
class Halbut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet
mary.pet = rover

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a pet
frank.pet = satan

# filpper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salman()

# harry is-a Halbut
harry = Halbut()