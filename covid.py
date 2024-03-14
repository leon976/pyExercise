temperature = float(input("Please enter your body temperature : "))

if temperature == 37.5:
    print("normal")
elif temperature > 37.5 and temperature < 39:
    print("its fever")
elif temperature >= 39:
    print("kubit")
else:
    print("please go to the hospital")


