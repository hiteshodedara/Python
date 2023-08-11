#Assertion in python...

print("\nAssertion...\n")


def func(n):
    assert n<0, 'Only Nagative numbers are allowed...'
    print("You entered : ", n)

while True:
    num = int(input("\nEnter any nagative number : "))
    try:
        func(num)
    except AssertionError as msg:
        print(msg)
