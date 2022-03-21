class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        print("default init method")

#    def config(self):
 #       print("computer configuration")
    def config1(self):
        print("CPU core is", self.cpu, " memory size is ", self.ram)

comp2=computer(120,10)
comp2.config1()