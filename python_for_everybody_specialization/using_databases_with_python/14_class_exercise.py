# class is a reserved word that defines a template for making objects
# when an object is constructed, a specially named method is called to allocate and initialize attributes  

class Dog:                          # template
    def __init__(self):             # constructor method
        self.x = 0                  # attribute x

    def bark(self):                 # method
        self.x += 1
        print('Woof!')
        print()

    def times(self):                # another method
        return self.x
# all the code within the class defined Dog behaviour 


# construction of the Dog object
dg = Dog()

print('Type', type(dg))
print()
print('Dir ', dir(dg))
print()
print('Type', type(dg.x))
print()
print('Type', type(dg.bark))
print()
print('Type', type(dg.times))
print()

max_barks = 3

while dg.x < max_barks:
    data = int(input('Bark! '))
    
    if data == 0:
        break
    else:
        # tell the 'dg' object to run the bark() method within itself
        dg.bark()

# tell the 'dg' object to run the times() method within itself
print(dg.times())