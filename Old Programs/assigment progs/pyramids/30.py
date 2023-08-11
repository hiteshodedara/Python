n = int(input("Enter number of lines : "))


#for loop..
print("\n\nFor loop..\n")
b_space = int(0)
fpsapce = n*2-3
bpspace = int(1)
print("*"*(n*2+1) + " "*3 + "*")
for i in range(n-1):
    b_space += 1
    print(" "*b_space + "*" + " "*fpsapce + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpsapce -= 2
    bpspace += 2
print(" "*(b_space+1) + "*" + " "*3 + "*"*(n*2+1))



#while loop..
print("\n\nWhile loop..\n")
b_space = int(0)
fpsapce = n*2-3
bpspace = int(1)
i = int(0)
print("*"*(n*2+1) + " "*3 + "*")
while(i<n-1):
    b_space += 1
    print(" "*b_space + "*" + " "*fpsapce + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpsapce -= 2
    bpspace += 2
    i += 1
print(" "*(b_space+1) + "*" + " "*3 + "*"*(n*2+1))
