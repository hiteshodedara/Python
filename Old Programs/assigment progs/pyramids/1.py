a = int(input("Enter the number of lines : "))
n = int(a+1)

print("For loop\n")
#for loop
for i in range(int(n)):
    print("*"*i)

print("\n")

print("while loop\n")
#while loop
i=1
while(i<n):
    print("*"*i)
    i+=1
