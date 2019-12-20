"""
import math

x = float(input("Enter x: "))
y = math.sqrt(x)

print("The square root of",x,"equals to",y)
"""
"""
#ZeroDivisonError
try:
    print("1")
    x = 1/0
    print("2")
except:
    print("Oh dear, something went wrong...")
print("3")
"""
"""
try:
    x = int(input("Enter a number: "))
    y = 1/x
    print(y)
except ZeroDivisionError:
    print("You can´t devide by zero, sorry.")
except ValueError:
    print("You must enter an interger value.")
except:
    print("Oh dear, something went wrong...")
print("THE END")
"""
#the order matters
try:
    y = 1/0
except ZeroDivisionError:
    print("Zero Division")
except ArithmeticError:
    print("Arithmetic Error")
print("THE END")