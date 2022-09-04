n = int(input("Enter number to make pyramid : "))

b = n
space = int(1)
#for loop..
print("\nFor loop...")
print(" "*b + "*")
for i in range(n-1):
    b -= 1
    print(" "*b + "*" + " "*space + "*")
    space += 2
space -= 4
for i in range(n-2):
    b += 1
    print(" "*b + "*" + " "*space + "*")
    space -= 2
print(" "*(b+1) + "*")


#while loop...
print("\nWhile loop...")
b = n
space = int(1)
print(" "*b + "*")
i = int(0)
while(i < n-1):
    b -= 1
    print(" "*b + "*" + " "*space + "*")
    space += 2
    i += 1
i = int(0)
space -= 4
while(i<n-2):
    b += 1
    print(" "*b + "*" + " "*space + "*")
    space -= 2
    i += 1
print(" "*(b+1) + "*")
