from classeA import ClasseA

class ClasseC(ClasseA):
    def m1(self):
        super().m1()
    def m2(self):
        print(f"Método C")