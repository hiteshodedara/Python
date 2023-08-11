n = int(input("Enter number of lines : "))


#for loop...
print("\n\nFor loop...\n")
f_space = n
fpspace = int(1)
bpspace = n*2-3
print(" "*f_space + "*" + " "*3 + "*"*(n*2+1))
for i in range(n-1):
    f_space -= 1
    print(" "*f_space + "*" + " "*fpspace + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpspace += 2
    bpspace -= 2
print("*"*(n*2+1) + " "*3 + "*")


#while loop..
print("\n\nWhile loop...\n")
f_space = n
fpspace = int(1)
bpspace = n*2-3
i = int(0)
print(" "*f_space + "*" + " "*3 + "*"*(n*2+1))
while(i< n-1):
    f_space -= 1
    print(" "*f_space + "*" + " "*fpspace + "*" + " "*3 + "*" + " "*bpspace + "*")
    fpspace += 2
    bpspace -= 2
    i += 1
print("*"*(n*2+1) + " "*3 + "*")
