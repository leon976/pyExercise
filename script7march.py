# class Person:
#     #method (like a function reside in a class)
#     def display (self):
#         print('i am a person')

#     def greet (self):
#         print('hello, how are you')

# p1 = Person()
# p2 = Person()

# p1.display()
# p1.greet()

# p2.display()
# p2.greet()


# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def info(self):
#         print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

#     def make_sound(self):
#         print("Meow")

# name = input("cat name 1: ")
# age = input("cat age 1: ")

# name2 = input("cat name 2: ")
# age2 = input("cat age 2: ")

# cat1 = Cat(name, age)
# cat2 = Cat(name2, age2)

# cat1.info()
# cat1.make_sound()

# cat2.info()
# cat2.make_sound()

# class Car:
#     def __init__(self, color, size, model):
#         self.color = color
#         self.size = size
#         self.model = model
#         self.speed = 0  # initial speed is set to 0

#     def start_engine(self):
#         print("engine started")
    
#     def accelerate(self, speed_increase):
#         self.speed += speed_increase
#         print(f"car accelerated. current speed: {self.speed} km/h")

#     def brake(self, speed_decrease):
#         self.speed -= speed_decrease
#         print(f"car is slowed down. current speed: {self.speed} km/h")

#     def honk_horn(self):
#         print("beep! beep!")

# #create car object
# my_car = Car(color="Red", size="small", model="sedan")

        