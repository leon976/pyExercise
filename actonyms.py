import random
#acronyms = ['lol','idk','smh','tbh']
#for x in acronyms:
#    print(x)

r1 = random.random()
print(r1)

r2 = random.choice([1,2,3,4,5])
print(r2)

r3 = random.randint(1,2000)
print(r3)

#r4 = random.randint([2,45,768,345,0])
#print(r4)

total = 0
expense = []
for i in range(5):
    expense.append(float(input("enter a number : ")))

total = sum(expense)
print("total ", total)

#roll = random.randint(1,3)
#print(roll)
#if roll

def greeting(name,day):
    print("hello " + name +" this day is " + day)

    name = input("your name")
    today = input("wether today is good ot bad?")
    greeting(name,today)

    def complexCal(x,y,z):
        print(x * y * z)

        x = 2
        y = 3
        z = 6
        complexCal(x,y,z)