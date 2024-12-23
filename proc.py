class A:
    __x=10
    def __show(self):
        print("From Class A")
class B(A):
    pass
print(dir(B)) 
obj=B()
print(obj._A__x)       