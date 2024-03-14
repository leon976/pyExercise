import random

print("""
___.           .__                .__               .__          __                
\_ |__   _____ |__|   ____ _____  |  |   ____  __ __|  | _____ _/  |_  ___________ 
 | __ \ /     \|  | _/ ___\\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \
 | \_\ \  Y Y  \  | \  \___ / __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/
 |___  /__|_|  /__|  \___  >____  /____/\___  >____/|____(____  /__|  \____/|__|   
     \/      \/          \/     \/          \/                \/                   
      """)

quotes = random.choice (["eat healthy!", "health is happines", "be healthy!"])
print(quotes)

def calculate_bmi(weight, height):
    
    bmi = weight / (height * height)
    return bmi

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = calculate_bmi(weight, height)
print("Your BMI is:", bmi)

if bmi < 18.5:
    print("underweight")
elif 18.5 <= bmi <= 24.9:
    print("normal")
elif 18.5 <= bmi <= 24.9:
    print("overweight")
else:
    print("obese")
