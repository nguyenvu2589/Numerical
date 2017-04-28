import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import time

def actual_result(func, val):
	x = Symbol('x')
	dfunc = diff(func, 'x')
	x = val
	return eval(str(dfunc))

def three_point(func, x, h):
	x = x+h
	funcxh = eval(str(func))
	x = x-2*h
	funcxmh = eval(str(func))
	return (funcxh - funcxmh)/(2*h)

def plot(Result3Point,Error3Point):
	plt.plot(Result3Point,'k:',label= "3 Point")
	plt.plot(Error3Point,'k--',label= "3 Point Error")

	legend = plt.legend(loc='upper center', shadow=True)
	frame = legend.get_frame()
	frame.set_facecolor('0.90')
	plt.title('Three Point')
	plt.show()

def threePoint(func, x ,h):
    Result3Point= []
    Error3Point = []
    start = time.time()
    actualResult = actual_result(func, x)
    for item in h:
        Result3Point.append(three_point(func, x, item))

    Error3Point = np.asarray(Result3Point) - actualResult

    end = time.time()
    timeElapsed = end-start
    print ("Elapsed time: %f" % timeElapsed)
    print (Result3Point)

    plot(Result3Point, Error3Point)

if __name__ =='__main__':
	threePoint(sin('x'),0.0,[0.1,0.01,0.001])

