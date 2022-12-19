import math  # Imports math library (used for basic calculations) and the sympy library (used for many calculus
# functions).
import sympy

from sympy import *

x, y = symbols('x y')  # This defines what symbols are being used an not functions

def f(x):
    return #[INSERT FUNCTION HERE]
def findDir(a):
    foundDir = diff(a, x)
    print(foundDir)
print("The dirivative is: ")
findDir(f(x))