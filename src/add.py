

class Calculator:

    def __init__(self):
        print("Calculator class Sucessfully Created")

    def add(self,a,b):
        return a+b

if __name__ == '__main__':
    c = Calculator()
    print(c.add(1,2))