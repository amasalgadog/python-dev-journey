# Animal class is the superclass between Animal and Dog
class Animal:
    def __init__(self, name):
        self.name = name
        self.total_sleep = 0
        print()
        print('Welcome!', self.name)

    def sleep(self, time):
        self.total_sleep += time
        print('Zzzzz...')

    def drink_water(self):
        print('Slurp! Slurp!')

# Dog class is subclass of Animal class
# Dog inherit the behaviour and attributes of Animal class
class Dog(Animal):
    def __init__(self, name):
        # super() refers to Animal class and __init__() call its constructor method
        super().__init__(name)
        self.total_barks = 0

    def bark(self):
        self.total_barks += 1
        print('Woof!')

        # every 3 times Dog barks, it has to sleep 5 hours
        if self.total_barks % 3 == 0 and self.total_barks > 0:
            self.sleep(5)

        # one bark after sleep, Dog has to drink water
        if self.total_barks % 4 == 0 and self.total_barks > 0:
            self.drink_water()

an = Animal('Trini')
an.drink_water()
an.sleep(3)

dg = Dog('Pelu')
dg.bark()
dg.bark()
dg.bark()
dg.bark()
dg.bark()
