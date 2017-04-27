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
    sum=0    
    part1=(0.5)*h*(f(a)+f(b))
    for i in range(1,n):
        xi=a+i*h
        sum=sum+f(xi)
        array.append(part1+h*sum)
    return part1+h*sum, array

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
        return approx

def plot(array):
    plt.plot(array,'k--',label= "Trapezoidal")
    legend = plt.legend(loc='upper center', shadow=True)
    
    plt.show()

def error_trap(func,a,b,n):
    h=(b-a)/n
    c =  derivative(func, float(a+b)/2 , n =2)
    return (((b-a)**2)* (h**2) * c)/ 25

def error_simp(func,a,b,n):
    actual = integrate.quad(func, 0, 1)[0]
    approx = newtonSimpson(func, a, b, n)
    return round(abs(actual - approx),8)

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

if __name__ == '__main__':
    func = lambda x: x**2
    a = 0.0
    b = 1.0
    n = 4

    newtTrapSimp(func, a, b, n)



