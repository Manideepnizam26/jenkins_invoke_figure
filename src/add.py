import sys

class Calculator:

    def __init__(self):
        print("Calculator class Sucessfully Created")

    def add(self,a,b):
        return a+b

if __name__ == '__main__':
    number_of_params_passed = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    print("a:",a)
    print("b:",b)
    calc = Calculator()
    print(calc.add(a,b))