import numpy as np
import matplotlib.pyplot as plt


#arr=np.array([[1,8,5],[9,6,4]])

#print("size=",arr.dtype)
#str="hello"

#print(np.char.replace("hello loooo","hello","hi"))


#hi=np.char.encode("hello",'cp500')
#bi=np.char.decode(hi,'cp500')
#print(hi)
#print(bi)


#a=np.char.center('hi',20,fillchar="*")
#print(a)


#a=np.char.count(str,"hello")
#print(a)


#a=np.sort(arr)
#print(a)


#a=np.arange(9,4,6)
#print(a)


x=np.array([1,6])
y=np.array([2,5])

plt.xlabel("X")
plt.ylabel("Y")

plt.title("demo plt")

plt.plot(x,y,marker="*",ms=20)
plt.show()
