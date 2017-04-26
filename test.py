import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import time
import io
import sys
from chebyshev import chebyshev
from cubicsplines import cubicSpline
from leastSquares import leastSquares
from bezier import bezier
from nonlinearleastsquares import nonLinearLeastSquares
from differencemethods import differenceMethods
from extrapolation import extrapolation
from autodiff import autoDiff
from trapezoidalsimpson import newtonTrapezoidal
from trapezoidalsimpson import newtonSimpson
from romberg1 import romberg
from adaptive import adaptive
from gaussian import gaussian

categories = ['Chebyshev', 'Cubic Splines', 'Bezier', 'Linear Least Squares', 'Nonlinear Least Squares',
              'Difference Methods', 'Extrapolation', 'Automatic Differentiation', 'Newton-Cotes: Trapezoidal',
            'Newton-Cotes: Simpson', 'Romberg', 'Adaptive', 'Gaussian']

def cbc(id, tex, input):
    return lambda : callback(id, tex, input)

def callback(id, tex, input):
    out = io.StringIO()
    sys.stdout = out
    tex.delete("1.0",tk.END)
    try:
        dispatcher={'chebyshev':chebyshev, 'cubicSpline':cubicSpline, 'leastSquares': leastSquares, 'bezier':bezier,
                    'nonLinearLeastSquares':nonLinearLeastSquares, 'differenceMethods':differenceMethods, 'extrapolation':extrapolation,
                    'autoDiff':autoDiff, 'newtonTrapezoidal':newtonTrapezoidal, 'newtonSimpson':newtonSimpson, 'romberg':romberg,
                    'adapative':adaptive, 'gaussian':gaussian}
        w=input.get()
        eval(w, {'__builtins__':None}, dispatcher)
    except:
        tex.insert(tk.END, "You have entered an invalid input\n")
    sys.stdout = sys.__stdout__
    tex.insert(tk.END, out.getvalue())
    tex.see(tk.END)             # Scroll if necessary

top = tk.Tk()
right = tk.Frame()
right.pack(side=tk.RIGHT, expand=1)
input = tk.Entry(right)
input.pack(side=tk.TOP, fill='x')
tex = tk.Text(right)
tex.pack(side=tk.BOTTOM, fill='x')
bop = tk.Frame()
bop.pack(side=tk.LEFT, fill='y', expand='true')
for k in range(0,13):
    tv = categories[k]
    b = tk.Button(bop, text=tv, command=cbc(k, tex, input))
    b.pack(fill="x")
tk.Button(bop, text='Exit', command=top.destroy).pack(fill='x')
top.mainloop()