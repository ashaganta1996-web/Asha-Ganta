#polymorphism
class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")
d=Dog()
c=Cat()
d.sound()
c.sound()

#payment system
class Payment:
    def pay(self):
        print("Processing payment")
class GooglePay(Payment):
    def pay(self):
        print("Payment using Google Pay")
class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")
p1=GooglePay()
p2=CreditCard()
p1.pay()
p2.pay()

#polymorphism through method overriding
class Vehicle:
    def start(self):
        print("Vehicle is starting")
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")
car1=Car()
bike1=Bike()
car1.start()
bike1.start()