#Method overriding in class 

class Parent:
    def method1(self):
        print("CLASS 1")
class Child(Parent):
    def method1(self):
        super().method1()
        print("Child Class")

c=Child()
c.method1()
