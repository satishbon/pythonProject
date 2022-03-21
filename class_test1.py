class computer:
    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config1(self):
        print("CPU core is", self.cpu, " memory size is ", self.ram)

comp2=computer(10,20)
comp2.config1()