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

obj_A = A()
obj_B = B()
obj_C = C()

print("\nClass A Methods:")
obj_A.method_A1()
obj_A.method_A2()
obj_A.common_method()

print("\nClass B Methods:")
obj_B.method_B1()
obj_B.method_B2()
obj_B.common_method()

print("\nClass C Methods:")
obj_C.method_C1()
obj_C.method_C2()
obj_C.common_method()
