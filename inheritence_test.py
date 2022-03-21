class A:
    def __init__(self):
        print("class A")
    def config1(self):
        print("configuration set 1")

#class B inheriting class A
class B(A):
    #just added to prove super
    #if there is no super then it will run only init method of class B and it wont  run init method of class A
    #we can add super method to call the methods from child class
    #calling constructor inside child class
    def __init__(self):
        super().__init__()
        print("class B")

    def config2(self):
        print("configuration set 2")
obj1=B()
obj1.config1()
obj1.config2()
