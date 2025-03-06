class A:
    def method_A1(self):
        print("Method A1 - Specific to Class A")

    def method_A2(self):
        print("Method A2 - Specific to Class A")

    def common_method(self):
        print("Common Method in Class A")

class B(A):
    def method_B1(self):
        print("Method B1 - Specific to Class B")

    def method_B2(self):
        print("Method B2 - Specific to Class B")

    def common_method(self):
        print("Common Method in Class B (Overridden)")

class C(B):
    def method_C1(self):
        print("Method C1 - Specific to Class C")

    def method_C2(self):
        print("Method C2 - Specific to Class C")

    def common_method(self):
        print("Common Method in Class C (Overridden)")

class Main:
    @staticmethod
    def main():
        obj_B = B()
        obj_C = C()

        super_ref_B = obj_B  # Superclass reference pointing to B's object
        super_ref_C = obj_C  # Superclass reference pointing to C's object

        print("\nCalling overridden method using superclass reference:")
        super_ref_B.common_method()  # Calls B's overridden method
        super_ref_C.common_method()  # Calls C's overridden method

Main.main()
