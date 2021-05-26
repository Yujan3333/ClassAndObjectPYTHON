#Multilevel inheriitance

class parent:
    def big(self):
        print('Parent')

class child(parent):
    def small(self):
        print('Child')
class grand(child):
    def sm(self):
        print("extra small")

c=grand()
c.big()
c.sm()
c.small()
