a=int(input("Enter First value = "))
b=int(input("Enter Second value = "))
c=int(input("Enter third value = "))

if a>b and a>c:
    print("First value is big")
elif b>a and b>c:
    print("second value is big")
elif c>a and c>b:
    print("third value is big")
else:
    print("2 or 3 value are same")
    
