#Multiple inheritance

class A:
    def read(self):
        print("CLASS 1")
class B:
    def write(self):
        print("CLASS 2")
class C(A,B):
    def hello(self):
        print("Hello world")
c=C()    #for child class obj
c.hello()
c.read()
c.write()

#issubclass(sub,sup)
print(issubclass(C,A))
print(issubclass(A,C))

# to check if the object is from the derived class or not
#isinstance(obj,class)
d=B()   #for parent class obj
print(isinstance(c,C))  #for c isobj of child class C
print(isinstance(d,C))  #for d is obj of parent class B
