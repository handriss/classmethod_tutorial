class MyClass():

    def some_instance_method(self, *args, **kwds):
        pass

    @classmethod
    def some_class_method(cls, *args, **kwds):
        pass

    @staticmethod
    def some_static_method(*args, **kwds):
        pass

# Instance methods:
# - az osztály egy példányát használja a függvény argumentumként

 #input()

class Person():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)

# if we create an instance of a person, we can print the person's name:
first = Person("Francis")
first.print_name()

second = Person("Claire")
second.print_name()

#input()

# - we do not need to provide the class instances as arguments since we are
# usually calling the method on the instance itself

# but we dont need to, this also works and is an instance method:
Person.print_name(Person("Doug"))

#------------------------------------------------------------------------------

# What if we want a method that interacts with classes, not instances of
# classes?

# lets say, we want to count the number of instances of a classes
# we might do it like this:

def number_of_instances(cls):
    return cls.number_of_smurfs

class Smurf():
    number_of_smurfs = 0

    def __init__(self, name):
        Smurf.number_of_smurfs += 1
        self.name = name

smurf1 = Smurf("Papa Smurf")
smurf2 = Smurf("Smurfette")
print(number_of_instances(Smurf))

# OK, so we have interacted with a class through a function, so what's wrong?
# this works, but our function is separated from the class to which it is
# related, which is a bad practice. The solution: class methods

class Smurf2():
    number_of_smurfs = 0

    def __init__(self, name):
        Smurf2.number_of_smurfs += 1
        self.name = name

    @classmethod
    def number_of_instances(cls):
        return cls.number_of_smurfs

smurf1 = Smurf2("Brainy Smurf")
smurf2 = Smurf2("Vanity Smurf")
smurf3 = Smurf2("Handy Smurf")
print(number_of_instances(Smurf2))

# How do we use class methods?
# - rename self to cls (only convention)
#    (if we call this method from the instance, it will still contain the
#    instance of that class!)
#    but if we call from class, it will contain the class (regardless of the name)

# What are class methods good for?
# - they are good when we want to do stuff with classes without needing to create
# an instance of the class, for example:
# - we want to count the number of instances of a class (it needs to work at 0, too)
# - we want to change a "constant"
# - we want to read in a file and pass that information to the constructor

#-------------------------------------------------------------------------------

# What if want to create a method, that does not use a class, nor an instance
# of a class? In this case, we have the static methods!

# A static method may be connected to the class (for example it collects methods
# of the same logic), but it does not need the class, nor an instance of that class
# to work
# Static methods has no access to other parts of the class.

# Math
# Random
