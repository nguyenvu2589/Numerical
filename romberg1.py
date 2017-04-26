import numpy
import matplotlib.pyplot as plt
import math
from sympy import *

def romberg( f, a, b, n ):
    try: 
        r = numpy.array( [[0] * (n+1)] * (n+1), float )
        h = b - a
        r[0,0] = 0.5 * h * ( f( a ) + f( b ) )

        powerOf2 = 1
        for i in xrange( 1, n + 1 ):
            h = 0.5 * h
            sum = 0.0
            powerOf2 = 2 * powerOf2
            for k in xrange( 1, powerOf2, 2 ):
                sum = sum + f( a + k * h )

            r[i,0] = 0.5 * r[i-1,0] + sum * h

            powerOf4 = 1
            for j in xrange( 1, i + 1 ):
                powerOf4 = 4 * powerOf4
                r[i,j] = r[i,j-1] + ( r[i,j-1] - r[i-1,j-1] ) / ( powerOf4 - 1 )

        array = grab_data(r)
        print(r)
        plot(array)
        
    except:
        e = sys.exc_info()[0]
        write_to_page("<p>Error: %s</p>" % e)
        print('Sorry, you have not entered correct input')
        return -1
    #return r

def grab_data(romberg):
    i = 0
    array = []
    for item in romberg:
        array.append(item[i])
        i = i+ 1
    return array

def plot(array):
    plt.plot(array, 'ro')
    plt.xlabel('X Value')
    plt.ylabel('Y Value')
    plt.grid(True)
    plt.ion()
    plt.pause(0.001)
    plt.show()


# if __name__ == '__main__':
#     f = lambda x: sin(x)
#     a = 0
#     b = 2
#     n = 10
#     r= romberg(f, a, b, n)
    # array = grab_data(r)
    # print r
    # plot(array)



