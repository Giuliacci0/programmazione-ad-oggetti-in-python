#classe e istanza - stampa leggibile str
import weakref
class Book:
    books =[]
    def __init__ (self, n_pages, author, title):
        self.n_pages = n_pages
        self.author = author
        self.title = title
        self.__class__.books.append(weakref.proxy(self))
    def __str__ (self):
        return f"""N of pages: {self.n_pages} 
Author: {self.author} 
Title: {self.title}"""
    def book_info(self):
        return f"Book info:\nTitle: {self.title}\nAuthor: {self.author}\n"

libro1 = Book(1300, "Tolkien", "The Lord of the Rings")
libro2 = Book(150, "Tolstoy", "Sonata a Kreutzer")
libro1.title = "The hobbit"
print(libro1.title)
print(libro1)
print(Book.book_info(libro1))
print(libro2.book_info())


#stampa tutte le istanze della classe tramite weakref e 
#in init lista + self.__class__.lista.append(weakref.proxy(self))
def all_books():
    for instance in Book.books:
        print(instance)
all_books()


#super() per child class 
class Parent:
    def __init__(self, txt):
        self.message = txt
    def printmessage(self):
        print(self.message)
class Child(Parent):
  def __init__(self, txt, child_attr):
    super().__init__(txt)
    self.child_attr = child_attr
    
x = Child("Hello, and welcome!", "child attribute")
x.printmessage()
print(x.child_attr)


""" Ex. 1 create a class with two attributes"""
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
    
model1 = Vehicle(400, 16)
print(f"Model1 max speed is {model1.max_speed}, its mileage is {model1.mileage}")

""" Ex. 2 Create a Vehicle class without any variables and methods"""
class Vehicle:
    pass

""" Ex. 3 Create a child class Bus that will inherit all of the variables and methods of the Vehicle class"""
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:", School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

""" Ex 4 Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50"""
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())

""" Ex 5  Define a property that must have the same value for every class instance (object)"""
#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
class Vehicle:
    #attributo di classe
    color = "White"
    def __init__(self, name, max_speed, mileage):
        
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass
mod_1 = Bus("School Volvo", 180, 12)
mod_2 = Car("Audi", 240, 18)

def print_models():
    print(f"Color: {mod_1.color}, Name: {mod_1.name}, Speed: {mod_1.max_speed}, Mileage: {mod_1.mileage}")
print_models()

""" Ex 6 Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become 
the final amount = total fare + 10% of the total fare.
Note: The bus seating capacity is 50. so the final fare amount should be 5500. You need to override the fare() method of a Vehicle class 
in Bus class.
"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

"""class Bus(Vehicle):
    def fare(self):
        perc = super().fare() * 10 / 100
        return super().fare() + perc"""
class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount
School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

""" Ex 7 Write a program to determine which class a given Bus object belongs to """
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(type(School_bus))

""" Ex 8 Determine if School_bus is also an instance of the Vehicle class       ISINSTANCE()"""
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)
print(isinstance(School_bus, Vehicle))