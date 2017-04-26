import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import time
from math import *

def ti1(f,a,b):
    return ((b-a)/2)*(f(a)+f(b))

def diff2(f,x,h=1E-6):
    r=(f(x-h)-2*f(x) + f(x+h))/float(h*h)
    return r
    
def trapezint(f,a,b,n):
    array =[]
    h=(b-a)/n
    sum=0
    part1=(0.5)*h*(f(a)+f(b))
    for i in range(1,n):
        xi=a+i*h
        sum=sum+f(xi)
        array.append(part1+h*sum)
    return part1+h*sum, array

def Simpson(f, a, b, n):
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

def adaptive(f,a,b,ep):
    max=0 
  
    step=float(abs(a-b)/1000)
    i=0
    while (i<1000):
        i=i+1

        adj=a
        adj=a+step*i
        dval=diff2(f,adj)
        if(abs(dval)>max):
            max=abs(dval)
            
    h=sqrt(12*ep)*((b-a)*max)**.5
    n=(b-a)/h        
    return trapezint(f,a,b,int(ceil(n))),Simpson(f,a,b,int(ceil(n))),i

def plot(array):
    plt.plot(array,'k--',label= "Trapezoidal")
    legend = plt.legend(loc='upper center', shadow=True)
    
    plt.show()


def main():
	func = lambda x: x**2
	a = 0.0
	b = 1.0
	ep = 0.005
	#print trapezint(func, a, b, 10)
	Atrap,Asimp,i = adaptive(func,a,b,ep)
	print("this is Adaptive trapezoid" ,round(Atrap[0],8))
	print("this is Adaptive Simpson" ,round(Asimp,8))
	plot(Atrap[1])
	 
if __name__ =='__main__':
	main()



