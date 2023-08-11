#Abstraction, Inheritance, Encaptulation in python 

print("Abstraction, Inheritance, Encaptulation in python....\n\n")

class Fruits():
    _income = 0  #protected data
    def price(self):
        pass    #abstract method
    def buy(self, fru, q, p):
        Fruits._income += q * p
        print(q , "kg", fru, "are sold...")
        print(q*p, " Rs. collected...")
        print(f'Total income is {Fruits._income} Rs.')

class Banana(Fruits):
    def price(self):
        print("Banana price is 50 Rs. per KG...")
    
class Apple(Fruits):
    def price(self):
        print("Apple price is 60 Rs. per KG...")

class Mango(Fruits):
    def price(self):
        print("Mango price is 100 Rs per KG...")


class Kiwi(Fruits):
    def price(self):
        print("Kiwi price is 150 Rs per KG...")

class Orange(Fruits):
    def price(self):
        print("Orange price is 40 Rs per KG...")


while True:

    print("\n\nFruits shop...")
    print("What do you want ")
    print("1. see the prices of available fruits... ")
    print("2. buy available fruits... ")
    print("3. exit from the shop")

    i = int(input("Enter your choice : "))

    if i == 1:
        print("we have these fruits...")
        print("1. Banana")
        print("2. Apple")
        print("3. Mango")
        print("4. Kiwi")
        print("5. Orange")

        i = int(input("which price you want to know : "))

        if i == 1:
            f = Banana()
            f.price()
        elif i == 2:
            f = Apple()
            f.price()
        elif i == 3:
            f = Mango()
            f.price()
        elif i == 4:
            f = Kiwi()
            f.price()
        elif i == 5:
            f = Orange()
            f.price()
        else :
            print("Wrong choice....")

    elif i == 2:
        print("we have these fruits...")
        print("1. Banana")
        print("2. Apple")
        print("3. Mango")
        print("4. Kiwi")
        print("5. Orange")

        i = int(input("which price you want to know : "))
        q = int(input("How much kg do you want to buy : "))
        f = Fruits()

        if i == 1:
            f.buy('Banana', q, 50)
        elif i == 2:
            f.buy('Apple', q, 60)
        elif i == 3:
            f.buy('Mango', q, 100)
        elif i == 4:
            f.buy('Kiwi', q, 150)
        elif i == 5:
            f.buy('Orange', q, 40)
        else :
            print("Wrong choice....")
    
    elif i == 3:
        break
    else :
        print("wrong choice...")
