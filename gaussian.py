import numpy as np
from scipy.integrate import fixed_quad
import matplotlib.pyplot as plt

### aware that precision is 2n-1

def gaus_quad(func, a, b, n):
    return fixed_quad(func, a, b, n)


def main():
    func = exp(-x**2/2)
    gaus_quad(func, -1, 1, 4)
    return 0


def gaussian(x,y,z):
    return 0


if __name__ == '__main__':
    main()
