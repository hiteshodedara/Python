class hi:
    def __init__(self,name=None,city=None,email=None):
        self.name=name
        self.city=city
        self.email=email

    def show(self):
        print(self.name)
        print(self.city)
        print(self.email)


q=hi("hitesh","email@","jun")
q.show()