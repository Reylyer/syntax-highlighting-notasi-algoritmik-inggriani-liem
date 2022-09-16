# %%
from sympy import exp, nsolve, Eq, diff, sin, cos
from sympy.abc import x
import numpy as np
import pandas as pd
import warnings

MAX_ITER = 200
TOL      = 10**(-5)


def newton_raphson( f, f_prime, x_c, tol):
    df = pd.DataFrame({ 'x_c'    : pd.Series(dtype='float'),
                        'f(x_c)' : pd.Series(dtype='float'),
    })
    deltas = []

    df.loc[len(df.index)] = [x_c, f(x_c)]

    # Loop sampai kita mencapai TOLERANSI atau kita mengambil MAX_STEPS
    for iter in range(1, MAX_ITER + 1):
        x_prev = x_c
        x_c = x_c - f(x_c) / f_prime(x_c)

        deltas.append(abs(x_c - x_prev))
        df.loc[len(df.index)] = [x_c, f(x_c)]

        if np.abs(f(x_c)) < tol:
            break

    else:
        warnings.warn('Jumlah maksimum langkah yang terlampaui')

    deltas.append("")
    df["delta"] = deltas
    df.to_excel("newtonraphson.xlsx", engine='openpyxl')
    return x_c, iter

# %%
if __name__ == "__main__":
    #f(x) =    e^x + x^2  - 3x  - 2
    # f_x   = exp(x) + x**2 - 3*x - 2
    # f_x = x**3 - 2*x -5
    # f_x = sin(x) - 1 + x
    f_x = x**3 + 4*x + 1
    f_x_prime = diff( f_x, x, 1)
    
    f_x_subs = lambda a: float(f_x.subs(x, a))
    f_x_prime_subs = lambda a: float(f_x_prime.subs(x, a))
    f_eq = Eq( f_x,  0)

    print("akar dari nsolve :", nsolve( f_eq, x, -1) )

    akar, it = newton_raphson(f_x_subs, f_x_prime_subs, 1, TOL)
    print(f"akar pendekatan  : {akar} dengan {it} iterasi")