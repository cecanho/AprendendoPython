from classeB import ClasseB
from classeC import ClasseC

class ClasseD(ClasseB, ClasseC):
    def m1(self):
        super().m1()

    def m2(self):
        super().m2()