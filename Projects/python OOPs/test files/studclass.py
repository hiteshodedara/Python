class data:
    def var(self,n,e,r,c):
        self.name=n
        self.email=e
        self.city=c
        self.rno=r

class student1(data):
    def show(self):
        print(self.name)
        print(self.email)
        print(self.rno)
        print(self.city)



st=student1()
st.var("hitesh","email",45,"juna")
st.show()

        