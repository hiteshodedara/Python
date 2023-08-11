n = int(input("Enter the number of lines : "))

print("\nFor loop...")
#for loop
for i in range(1,int(n+1)):
    print("*"*i)
for i in range(int(n-1),0,-1):
    print("*"*i)


print("\nwhile loop..")
#while loop
i=1
while(i<n):
    print("*"*i)
    i+=1
while(i>0):
    print("*"*i)
    i-=1

