class A:
    def __init__(self):
        self.value = "Value from Class A"

class B(A):
    def __init__(self):
        super().__init__()
        self.value = "Value from Class B"

class C(B):
    def __init__(self):
        super().__init__()
        self.value = "Value from Class C"

class Main:
    @staticmethod
    def main():
        obj_B = B()
        obj_C = C()

        super_ref_B = obj_B  # Superclass reference to B’s object
        super_ref_C = obj_C  # Superclass reference to C’s object

        print("\nAccessing data members using superclass reference:")
        print("super_ref_B.value:", super_ref_B.value)  # Accesses B's value
        print("super_ref_C.value:", super_ref_C.value)  # Accesses C's value

Main.main()
