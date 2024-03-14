#Q1
#name = input("Please enter your name : ")
#matNum = input("Please enter your Matrix Number : ") 
#classs = input("please enter your class : ")
#phoneNum = input("please enter your phone number : ")

#print ("*************************")
#print ("*   my personal info    *")
#print ("*************************")
#print ("1. Name         : ", name)
#print ("2. Matric Number: ", matNum)
#print ("3. class        : ", classs)
#print ("4. Phone Number : ", phoneNum)


#Q2
#def convert(sec):
    
#    minutes = sec // 60
#    remainingSec = sec % 60
    
#    print(f"{sec} seconds is equal to {minutes} minutes and {remainingSec} seconds.")

#secinput = float(input("convert seconds to numbers: "))
#convert(secinput)

#Q3
# i1 = 2
# i2 = 5
# i3 = -3
# d1 = 2.0
# d2 = 5.0
# d3 = -0.5
# a = i1 + (i2 * i3)
# b = i1 * (i2 + i3)
# c = i1 / (i2 + i3)
# d = i1 // (i2 + i3)
# e = i1 / i2 + i3
# f = i1 // i2 + i3
# g = 3 + 4 + 5 / 3
# h = 3 + 4 + 5 // 3
# i = (3 + 4 + 5) / 3
# j = (3 + 4 + 5) // 3
# k = d1 + (d2 * d3)
# l = d1 + d2 * d3
# m = d1 / d2 - d3
# n = d1 / (d2 - d3)
# o = d1 + d2 + d3 / 3
# p = (d1 + d2 + d3) / 3
# q = d1 + d2 + (d3 / 3)
# r = 3 * (d1 + d2) * (d1 - d3)

# print ("result a : ",a)
# print ("result b : ",b)
# print ("result c : ",c)
# print ("result d : ",d)
# print ("result e : ",e)
# print ("result f : ",f)
# print ("result g : ",g)
# print ("result h : ",h)
# print ("result i : ",i)
# print ("result j : ",j)
# print ("result k : ",k)
# print ("result l : ",l)
# print ("result m : ",m)
# print ("result n : ",n)
# print ("result o : ",o)
# print ("result p : ",p)
# print ("result q : ",q)
# print ("result r : ",r)

#Q4
# def calculate(lenght):
    
#     res = lenght * 0.3937
#     return res

# lenght = float(input("Enter lenght in cm : "))


# res = calculate(lenght)

# if lenght < 0:
#     print("invalid lenght")
# else:
#     print("Your lenght in cm converted into inches is:", res)

#Q5
# def login():
#     passs = "0000"
#     tries = 5

#     while tries > 0:
#         ques = input("Enter the password: ")

#         if ques == passs:
#             print("You have successfuly logged in to the system.")
#             break
#         else:
#             tries -= 1
#             if tries > 0:
#                 print(f"Wrong password! {tries} attempts left.")
#             else:
#                 print("You are blocked from the system after five unsuccessful tries.")
#                 break

# login()

#Q6