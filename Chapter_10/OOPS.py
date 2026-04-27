# ============================================
# OBJECT ORIENTED PROGRAMMING IN PYTHON
# ============================================

# -------------------------------
# 1. CLASS & OBJECT
# -------------------------------
class Person:
    def __init__(self, name, age):   # constructor runs when object is created
        self.name = name             # instance variable (stored in object)
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")  # accessing object data


p1 = Person("Avinash", 21)   # object creation → calls __init__
p1.display()                 # method call


# -------------------------------
# 2. INSTANCE VARIABLES & METHODS
# -------------------------------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks      # return instance variable


s1 = Student("Rahul", 90)
print("Marks:", s1.get_marks())


# -------------------------------
# 3. CLASS VARIABLE
# -------------------------------
class Company:
    company_name = "Google"   # class variable (shared by all objects)

    def __init__(self, emp):
        self.emp = emp        # instance variable (unique per object)


c1 = Company("Aman")
c2 = Company("Rohit")
# c1.company_name="Ram"   we do like this

print(c1.company_name)   # both access same class variable
print(c2.company_name)


# -------------------------------
# 4. INHERITANCE
# -------------------------------
class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):   # Dog inherits Animal
    def bark(self):
        print("Dog barks")


d = Dog()
d.sound()   # inherited method
d.bark()    # own method


# -------------------------------
# 5. METHOD OVERRIDING
# -------------------------------
class Animal2:
    def sound(self):
        print("Animal sound")


class Cat(Animal2):
    def sound(self):   # overriding parent method
        print("Cat meows")


c = Cat()
c.sound()   # calls overridden method


# -------------------------------
# 6. MULTIPLE INHERITANCE
# -------------------------------
class A:
    def showA(self):
        print("Class A")


class B:
    def showB(self):
        print("Class B")


class C(A, B):   # inherits from both A and B
    def showC(self):
        print("Class C")


obj = C()
obj.showA()   # from A
obj.showB()   # from B
obj.showC()   # own


# -------------------------------
# 7. ENCAPSULATION (private)
# -------------------------------
class Bank:
    def __init__(self, balance):
        self.__balance = balance   # private variable (name mangling)

    def deposit(self, amount):
        self.__balance += amount   # modify private variable

    def get_balance(self):
        return self.__balance      # access via method


b = Bank(1000)
b.deposit(500)
print("Balance:", b.get_balance())


# -------------------------------
# 8. POLYMORPHISM
# -------------------------------
class Bird:
    def fly(self):
        print("Bird flies")


class Sparrow(Bird):
    def fly(self):   # same method name, different behavior
        print("Sparrow flies")


class Ostrich(Bird):
    def fly(self):
        print("Ostrich cannot fly")


# same method call, different outputs → polymorphism
for bird in [Sparrow(), Ostrich()]:
    bird.fly()


# -------------------------------
# 9. STATIC METHOD
# -------------------------------
class Math:
    @staticmethod
    def add(a, b):
        return a + b   # does not use self or class


print("Sum:", Math.add(5, 3))   # called without object


# -------------------------------
# 10. CLASS METHOD
# -------------------------------
class School:
    school_name = "ABC School"

    @classmethod
    def change_name(cls, name):   # cls refers to class
        cls.school_name = name    # modifies class variable


School.change_name("XYZ School")
print(School.school_name)


# -------------------------------
# 11. DUNDER METHODS (__str__)
# -------------------------------
class Car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):   # controls print output
        return f"Car brand is {self.brand}"


car = Car("BMW")
print(car)   # calls __str__ automatically


# -------------------------------
# 12. ABSTRACTION
# -------------------------------
from abc import ABC, abstractmethod

class Shape(ABC):   # abstract base class
    @abstractmethod
    def area(self):
        pass        # must be implemented in child


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b   # implementation of abstract method


r = Rectangle(4, 5)
print("Area:", r.area())


# -------------------------------
# 13. PROPERTY (GETTER/SETTER)
# -------------------------------
class Employee:
    def __init__(self, salary):
        self._salary = salary   # protected variable

    @property
    def salary(self):
        return self._salary     # getter

    @salary.setter
    def salary(self, value):
        if value > 0:           # validation
            self._salary = value


e = Employee(5000)
print(e.salary)   # calls getter

e.salary = 8000   # calls setter
print(e.salary)