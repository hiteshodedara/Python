n = int(input("Enter the number of lines : "))


#for Loop...
print("\nFor Loop...")
space = int(0)
print("*")
for i in range(n-1):
    if i == n-2 :
        print("*"*(space+int(2)))
    else:
        print("*" + " "*space + "*")
        space += 1

#While loop...
print("\nWhile loop...")
space = int(0)
print("*")
while(space < n-1):
    if space == n-2:
        print("*"*(space+int(2)))
        space += 1
    else :
        print("*" + " "*space + "*")
        space += 1
