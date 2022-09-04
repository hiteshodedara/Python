n = int(input("Enter the numberv of lines : "))

space = n-2

#for loop...
print("\nFor Loop..")
print(" "*(n-1) + "*")
i = int(1)
for j in range(n-1):
    if j == (n-2):
        print("*"*(i+2))
    else:
        print(" "*space + "*" + " "*i + "*")
        i += 2
        space -= 1


#while loop...
print("\nWhile Loop...")
space = n-2
print(" "*(n-1) + "*")
j = int(0)
i = int(1)
while(j<n-1):
    if j == (n-2):
        print("*"*(i+2))
        j += 1
    else:
        print(" "*space + "*" + " "*i + "*")
        i += 2
        j+=1
        space -= 1
