## module trapezoid
""" 
Inew = trapezoid(f,a,b,Iold,k).
Recursive trapezoidal rule:
old = Integral of f(x) from x = a to b computed by
trapezoidal rule with 2ˆ(k-1) panels.
Inew = Same integral computed with 2ˆk panels.
"""
def trapezoid(f, a, b, Iold, k):
    if k == 1:
        Inew = (f(a) + f(b))*(b - a)/2.0
    else:
        n = 2**(k -2 ) # Number of new points
        h = (b - a)/n # Spacing of new points
        x = a + h/2.0
        sum = 0.0
        for _ in range(n):
            sum = sum + f(x)
            x=x+h
        Inew = (Iold + h*sum)/2.0
        return Inew


""" 
I,nPanels = romberg(f,a,b,tol=1.0e-6).
Romberg integration of f(x) from x = a to b.
Returns the integral and the number of panels used.
"""
import numpy as np
def romberg(f,a,b,tol=1.0e-6):
    def richardson(r,k):
        for j in range(k-1,0,-1):
            const = 4.0**(k-j)
            r[j] = (const*r[j+1] - r[j])/(const - 1.0)
        return r

    r = np.zeros(21)
    r[1] = trapezoid(f,a,b,0.0,1)
    r_old = r[1]
    for k in range(2,21):
        r[k] = trapezoid(f,a,b,r[k-1],k)
        r = richardson(r,k)
        if abs(r[1]-r_old) < tol*max(abs(r[1]),1.0):
            return r[1],2**(k-1)
        r_old = r[1]
    print("Romberg quadrature did not converge")
