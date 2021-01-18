# authors Name : Guy Dahan & Lior Elisberg
# IDs: 208271734 & 3080832473

from newtonRapson import *
from secantMethod import *
from sympy import symbols


def find_polynomial_roots(p, start, end, step_size, tol=10 ** -6):
    a = start
    secant_roots = list()
    newton_roots = list()
    while a + step_size <= end:  # while current value is still in range
        b = a + step_size  # b is equal to the next step
        if p(a) * p(b) < 0:  # if sign changed between steps
            secant_roots.append(secant_method(p, a, b, tol))  # get the root for secant in range (a,b)
            newton_roots.append(newton_method(p, a, b, tol))  # get the root for newton in range (a,b)
        a = b  # a gets the next step
    return secant_roots, newton_roots


if __name__ == '__main__':
    step_size = 0.01
    # polynomial function input
    print('Insert Polynomial function :')
    f = input('Y = ')

    # start, end, step size inputs
    start = float(input('Insert start for computing range :\t'))
    end = float(input('Insert end for computing range :\t'))

    secant_roots, newton_roots = find_polynomial_roots(lambda x: eval(f), start, end, step_size)
    if secant_roots is None and newton_roots is None:
        print('No roots found in both methods')
    else:
        print('*' * 40)
        print(f'The roots in Secant Method is: {secant_roots}')
        print(f'The roots in  Newton-Raphson is: {newton_roots}')
