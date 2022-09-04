n = int(input("Enter number of lines : "))


#for loop..
print("\n\nFor loop...\n")
bs = int(1)
ins = n-3
print("*"*(n*2-1))
for i in range(n-2):
    print(" "*bs + "*" + " "*ins + "*" + " "*ins + "*")
    bs += 1 
    ins -= 1
print(" "*(n-1) + "*")


#while loop..
print("\n\nWhile loop..\n")
bs = int(1)
ins = n-3
i = int(0)
print("*"*(n*2-1))
while (i < n-2):
    print(" "*bs + "*" + " "*ins + "*" + " "*ins + "*")
    bs += 1 
    ins -= 1
    i += 1
print(" "*(n-1) + "*")
