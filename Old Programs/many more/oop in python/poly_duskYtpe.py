class st1:
    def exe(self):
        print("st1 is print...")


class st2:
    def exe(self):
        print("st2 is print...")

class ok:
    def code(self,it):
        it.exe()

ide=st1()
code2=ok()
code2.code(ide)