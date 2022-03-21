
class computer:
    # init is the default method to start whenever to call from object each time
    def __init__(self):
        print("init calling")
    def config(self):
        print("helo")

comp1 =  computer()
# passing object to the class
computer.config(comp1)
comp2 = computer()
#calling object with class
comp2.config()


