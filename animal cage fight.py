from lion import Lion
from tiger import tiger
from snake import snake

def main():

    # instantiate a lion
    simba = Lion(name="Simba")

    # instantiate a tiger
    tailung = tiger(name="Tailung")

    # instantiate a snake
    viperess = snake(name="Viperess")

    # fight simulation
    print("Let the fight begin!")
    print("----------------------------")
    simba.roar()
    simba.attack()
    print("----------------------------")
    tailung.roar()
    tailung.attack()
    print("----------------------------")
    viperess.hiss()
    viperess.attack()
    print("----------------------------")
    print("The fight is over!")

if __name__ == "__main__":
    main()
