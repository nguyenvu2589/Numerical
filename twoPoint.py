import numpy as np
from sympy import *
import matplotlib.pyplot as plt
import time
import math


def actual_result(func, val):
    dfunc = diff(func,'x')
    x = val
    return eval(str(dfunc))


def two_point(func, x, h):
    funcx = eval(str(func))
    x = x + h
    funcxh = eval(str(func))
    return (funcxh - funcx) / h


def plot(Result2Point, Error2Point):
    plt.plot(Result2Point, 'k--', label="2 Point")
    plt.plot(Error2Point, 'k', label="2 Point Error")
    plt.legend = plt.legend(loc='upper center', shadow=True)
    plt.title('Two Point')
    plt.show()

def twoPoint(func, x, h):
    Result2Point = []
    Error2Point = []
    start = time.time()
    actualResult = actual_result(func, x)
    for item in h:
        Result2Point.append(two_point(func, x, item))

    Error2Point = np.asarray(Result2Point) - actualResult

    end = time.time()
    timeElapsed = end - start
    print("Elapsed time: %f" % timeElapsed)
    print(Result2Point)
    plot(Result2Point, Error2Point)


if __name__ == '__main__':

    twoPoint(sin('x'), 1.0, [0.1, 0.01, 0.001])
