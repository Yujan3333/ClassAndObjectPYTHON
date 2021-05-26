#Abstraction in python
class emp:
    __count=0
    def __init__(self):
        emp.__count=emp.__count+1
    def display(self):
        print(emp.__count)

e=emp()
try:
    print(e.__count)
finally:
    e.display()