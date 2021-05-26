#Static member , Can call without making obj
class calc:

    @staticmethod
    def add(a,b):
        return a+b

print("Addition is" ,calc.add(1,2))