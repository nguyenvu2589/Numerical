import tkinter as tk
import timeit
import io
import sys
import traceback
import math
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
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

categories = ['Chebyshev', 'Cubic Splines', 'Bezier', 'Linear Least Squares', 'Nonlinear Least Squares',
              'Difference Methods', 'Extrapolation', 'Automatic Differentiation', 'Newton-Cotes: Trapezoidal',
            'Newton-Cotes: Simpson', 'Romberg', 'Adaptive', 'Gaussian']


def callback(tex, input):
    plt.clf()
    out = io.StringIO()
    sys.stdout = out
    tex.delete("1.0",tk.END)
    try:
        w=input.get()
        start = timeit.default_timer()
        exec(w)
        stop = timeit.default_timer()
        fig.canvas.draw()
        sys.stdout = sys.__stdout__
        tex.insert(tk.END, out.getvalue())
        tex.insert(tk.END, 'Runtime: ' + str(stop - start) + 'ms')
        tex.see(tk.END)  # Scroll if necessary
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        tex.insert(tk.END, str(e))
        tex.insert(tk.END, str(traceback.extract_tb(exc_traceback)))
        tex.insert(tk.END, "You have entered an invalid input. Select a function from the left for example input.\n")



root = tk.Tk()
root.wm_title('Numerical Analysis Project 2.2')
right = tk.Frame()
right.pack(side=tk.RIGHT, expand=1, fill=tk.BOTH)

# hack
tex = tk.Text()

inputframe = tk.Frame(right)
inputframe.pack(side=tk.TOP, padx=(0,8), pady=(8,8), fill=tk.X, expand=1)
inputlabel = tk.Label(inputframe, text='Input: ')
inputlabel.pack(side=tk.LEFT, padx=(0,4))

inputText = tk.StringVar()


def setInput(category):
    print(category)
    if category == 'Chebyshev':
        inputText.set('chebyshev(-1, 1, 0.5, math.sin)')
    elif category == 'Cubic Splines':
        inputText.set('cubicSpline(\'(-1,3), (0,5), (3,1), (4,1), (5,1)\')')
    elif category == 'Bezier':
        inputText.set('Not yet implemented')
    elif category == 'Linear Least Squares':
        inputText.set('Not yet implemented')
    elif category == 'Nonlinear Least Squares':
        inputText.set('Not yet implemented')
    elif category == 'Difference Methods':
        inputText.set('Not yet implemented')
    elif category == 'Extrapolation':
        inputText.set('Not yet implemented')
    elif category == 'Automatic Differentiation':
        inputText.set('Not yet implemented')
    elif category == 'Newton-Cotes: Trapezoidal':
        inputText.set('Not yet implemented')
    elif category == 'Newton-Cotes: Simpson':
        inputText.set('Not yet implemented')
    elif category == 'Romberg':
        inputText.set('Not yet implemented')
    elif category == 'Adaptive':
        inputText.set('Not yet implemented')
    elif category == 'Gaussian':
        inputText.set('Not yet implemented')
    else:
        print('Error')

userinput = tk.Entry(inputframe, textvariable=inputText)
userinput.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=(4,4))

fig = plt.figure(1)
canvas = FigureCanvasTkAgg(fig, master=right)
plt.ion()
plot_widget = canvas.get_tk_widget()
plot_widget.pack(side=tk.BOTTOM, fill=tk.BOTH)

txt_frm = tk.Frame(right)
txt_frm.pack(side=tk.RIGHT, fill="x", expand=True)
# ensure a consistent GUI size
txt_frm.grid_propagate(False)
# implement stretchability
txt_frm.grid_rowconfigure(0, weight=1)
txt_frm.grid_columnconfigure(0, weight=1)

tex = tk.Text(txt_frm, height=8)
tex.pack(fill='x', padx=(0,16))

executebutton = tk.Button(inputframe, text='Execute', command=lambda: callback(tex, userinput))
executebutton.pack(side=tk.RIGHT, padx=(4, 0))

scrollb = tk.Scrollbar(txt_frm, command=tex.yview)
scrollb.grid(row=0, column=1, sticky='nsew', padx=(16,0))
tex['yscrollcommand'] = scrollb.set

bop = tk.Frame(width=200)
bop.pack(side=tk.LEFT, fill='y', pady=(8, 8), padx=(8, 8))
for k in range(0, 13):
    tv = categories[k]
    b = tk.Button(bop, text=tv, command=lambda tv=tv: setInput(tv))
    b.pack(fill="x", pady=(2, 2))
tk.Button(bop, text='Exit', command=root.destroy).pack(fill='x')


def main():
    inputText.set("Select a button from the left for example input.")
    root.mainloop()

if __name__ == '__main__':
    main()
