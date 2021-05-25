class Parent:
    def __init__(self,LN,age,looks):
        self.LN=LN
        self.age=age
        self.looks=looks
    
    def getLN(self):
        return self.LN
    def getage(self):
        return self.age
    def  getlooks(self):
        return self.looks

class Child(Parent):
        def __init__(self,LN,age,looks,weight):
            super().__init__(LN,age,looks)
            self.weight=weight  

        def getweight(self):
            return self.weight

c=Child('honda',21,'good',20)
c.age=1
print(c.getLN())
print(c.getage())
print(c.getlooks())
print(c.getweight())
#Using .format
print("My name is {0}. My age is {1}. My looks are {2}. My weight is {3}".format(c.getLN(),c.getage(),c.getlooks(),c.getweight()))
