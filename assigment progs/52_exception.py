#Exception Handling in python....

print("\nException Handling...\n")

while True:
    try:
        i = int(input("Only numbers are allowed : "))
        print("You entered : ", i)
    except:
        print("Oops!!, that was not a valid number....")
    finally:
        print("Enter number again....")
