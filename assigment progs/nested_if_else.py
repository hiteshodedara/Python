age = int(input("Enter your age : "))

if age<18:
    print("You are not eligible for voting...")
    if age<10:
        print("You are not eligible for covid vaccination...")
    else:
        print("You are eligible for vaccination...")
    
else:
    print("You are eligible for voting...")
    if age<32:
        print("You are eligible for GPSC exam...")
    else:
        print("You are not eligible for GPSC exam...")
