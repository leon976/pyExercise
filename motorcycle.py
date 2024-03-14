class Motorcycle:
    def __init__(self, age, model, color):
        self.age = int(age)
        self.model = model
        self.color = color

    def show(self):
        print(f"A very nice motorcycle with color: {self.color}, age: {self.age}, and model: {self.model}.")

    def greet(self):
        print("The motorcycle is very old. Consider buying a new one.")

color = input("Color: ")
age = int(input("Age: "))
model = input("Model: ")

motor = Motorcycle(age, model, color)

if motor.age < 10:
    motor.show()
else:
    motor.greet()
