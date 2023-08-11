n = int(input("Enter the number of lines : "))


#for loop..
print("\nFor loop..")
b = int(4)
fp = 2*n-1
sp = int(1)
for a in range(n):
    print(" "*a + "*"*fp + " "*b + "*"*sp)
    fp -= 2
    sp += 2


#while loop...
print("\nWhile loop..")
a = int(0)
b = int(4)
fp = 2*n-1
sp = int(1)
while(a < n):
    print(" "*a + "*"*fp + " "*b + "*"*sp)
    fp -= 2
    sp += 2
    a += 1
