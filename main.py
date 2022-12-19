import math  # Imports math library (used for basic calculations) and the sympy library (used for many calculus
# functions).
import sympy

from sympy import *

x, y, = symbols('x y')  # This defines what symbols are being used an not functions


# function = input("What is your function? ")
# derivative = input("What is that functions first derivative? ")
# x0 = int(input("What is the initial guess? "))
# tolerance = int(input("What is the 7-digit accuracy is desired? "))
# epsilon = int(float(input("What is a number that you do not want to divide smaller then? ")))
# max_iterations = int(input("What is the maximum number of iterations you want? "))

pi = math.pi
sqrt = sympy.sqrt

def f(x):
    return sqrt((((-1*cos(pi/3))*(60*x)+75))-((cos((pi/6)*x)*20)+(((-16*(x**2))-sin(pi/3)*(60*x))-(20*sin(6*(pi/6))+20)))) # f(x) = Inputted function


def f_prime(x):
    return (16*x + 5*pi*sin(pi*x/6)/3 - 15 + 15*sqrt(3))/sqrt(16*x**2 - 30*x + 30*sqrt(3)*x - 20*cos(pi*x/6) + 95)  # f'(x) = Inputted derivative


def newton(func, df, x0, tol):  # This output is an estimation of the root of f.
    if abs(func(x0)) < tol:  # This sees if the function is over the tolerance
        return x0
    else:
        return newton(f, df, x0 - f(x0) / df(x0), tol)


answer = (newton(f, f_prime, 1, 10))
fAnswer = str(f(answer))

print("The answer for x (in degrees) is: ")
print(math.degrees(answer))  # Prints the answer in decimal form
print(" ")
print("The answer for x (in radians) is: ")  # Prints the answer in radian form
print(answer)
print(" ")
print("And if we plug this value into the original function, we see that the local minimum is " + fAnswer)