# Warm-up exercises:
# A bit of arithmetic: some basics:
    # • Declare two variables x and y.
    # • Perform addition, subtraction, multiplication, and division.
    # • Print each result using print.
def warm_up():
    x = 10
    y = 2
    print(x+y, x-y, x*y, x/y)
# warm_up()

# Pythagorean Theorem : Write a program that solves the Pythagorean theorem! Your
# program should implement the following steps:
    # • Include the sqrt function from the module math via from math import sqrt.
    # • Declare two variables a and b and assign positive numeric values.
    # • Declare the variable c and assign sqrt(a*a + b*b) to it.
    # • Print the result c using print.
from math import sqrt
def sq():
    print(sqrt(4))

    a = 10
    b = 2
    c = sqrt(a*a + b*b)
    print(c)
sq()