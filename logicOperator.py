temperature =  float(input("Please enter your temperature : "))
forecast =  input("what is the forecast: ")

if temperature < 80 and forecast != "rain":
    print("go outside")
else:
    print("stay inside its not a good weather! <3")