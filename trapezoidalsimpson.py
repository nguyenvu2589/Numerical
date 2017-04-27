import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import time
from math import *
from scipy.misc import derivative
import scipy.integrate as integrate

global iteration

def newtonTrapezoidal(f,a,b,n):
    array = []
    h=(b-a)/n
    trapezoidalSum=0
    part1=(0.5)*h*(f(a)+f(b))
    for i in range(1,n):
        xi=a+i*h
        trapezoidalSum=trapezoidalSum+f(xi)
        array.append(part1+h*trapezoidalSum)

    plt.plot(array, 'k--', label="Trapezoidal")
    plt.legend(loc='best')

    print('Trapezoidal result: ' + str(part1+h*trapezoidalSum))

    h = (b - a) / n
    c = derivative(f, float(a + b) / 2, n=2)
    error = (((b - a) ** 2) * (h ** 2) * c) / 25

    print('Trapezoidal error: ' + str(error))


def newtonSimpson(f, a, b, n):
    if a > b:
        print('Incorrect bounds')
        return None
    else:
        if n%2 != 0: 
            n = n+1
        h = (b - a)/float(n) 
        sum1 = 0
        for i in range(1, int(n/2 + 1)):
            sum1 += f(a + (2*i - 1)*h)
        sum1 *= 4
        sum2 = 0
        for i in range(1, int(n/2)):
            sum2 += f(a + 2*i*h)
            
        sum2 *= 2
        approx = (b - a)/(3.0*n)*(f(a) + f(b) + sum1 + sum2)
        print ('Simpson result: ' + str(approx))

        actual = integrate.quad(f, 0, 1)[0]
        error = round(abs(actual - approx), 8)
        print ('Simpson error: ' + str(error))


<<<<<<< HEAD
def newtTrapSimp(func, a, b, n):
    #### SIMPSON
    print("This is Composite Simpson: " + str(round(newtonSimpson(func, a, b, n), 8)))
    print("This is Composite Simpson Error: " + str(round(error_simp(func, a, b, n), 8)))

    ### TRAPEZOIDAL
    result, array = newtonTrapezoidal(func, a, b, n)
    print("This is Composite Trapezoid: " + str(round(result, 8)))
    print("this is Composite Trapezoid Error: " + str(round(error_trap(func, a, b, n))))
    ### PLOT
    plot(array)

=======
>>>>>>> origin/master
if __name__ == '__main__':
    func = lambda x: x**2
    a = 0.0
    b = 1.0
<<<<<<< HEAD
    n = 4

    newtTrapSimp(func, a, b, n)

=======
    n = 10

    # SIMPSON
    newtonSimpson(func, a, b, n)
>>>>>>> origin/master

    # TRAPEZOIDAL
    newtonTrapezoidal(func, a, b, n)

