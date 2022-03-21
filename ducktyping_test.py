class duck:
    def fly(self):
        print("fly with wings")
class aeroplane:
    def fly(self):
        print("fly with fuel")

class car:
    def fly1(self):
        print("run with petrol")

# Attributes having same name are
# considered as duck typing
for obj in duck(),aeroplane(),car():
    obj.fly()