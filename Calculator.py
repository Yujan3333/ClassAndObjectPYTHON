class Calculator:
    
    def add(self,a=1,b=2,c=3,d=4,e=5):
        return a+b+c+d+e

    # def add(a):
    #     return a
    # def add(a,b):
    #     return a+b

c=Calculator()
print(c.add())
print(c.add(12,23,34,54,56))
print(c.add(10,20))
