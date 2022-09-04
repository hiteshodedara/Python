n = int(input("Enter the number of lines : "))

#for loop..
print("\nFor Loop...")
bspace = n-3
print("*"*n)
for aspace in range(1, n-1):
    print(" "*aspace + "*" + " "*bspace + "*")
    bspace -= 1
print(" "*(n-1)+ "*")

#while loop...
print("\nWhile Loop...")
bspace = n-3
print("*"*n)
aspace = 1
while(aspace<n-1):
    print(" "*aspace + "*" + " "*bspace + "*")
    bspace -= 1
    aspace += 1
print(" "*(n-1)+ "*")
