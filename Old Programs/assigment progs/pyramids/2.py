space = int(input("Enter the number of lines : "))
a = space + 1

print("\nfor loop...")
for n in range(a):
    print(" "*space,"*"*n)
    space-=1
 
n = 0
space = a - 1
print("\nwhile loop..")
while(n<a):
    print(" "*space,"*"*n)
    space-=1
    n += 1
