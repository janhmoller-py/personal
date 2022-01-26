"""
Functions:
fp: Fixed-point iteration method of finding the root of a function
nr: Newton-Raphson iteration method of finding the root of a function
lr: Left-hand rectangle Rule for approximating an integral
rr: Right-hand rectangle Rule for approximating an integral
mr: Midpoint rectangle Rule for approximating an integral
t: Trapezoidal Rule for approximating an integral
s: Simpson's Rule for approximating an integral

Use the help() command if use of any functions is unclear
"""


def fp(m, x0, n=0, lim=0.001):
    """
    A function for approximating the roots of a function using fixed point iteration
    Input:
    m: The fixed point form of the function for which you wish to approximate the root
    x0: The initial value of the the iteration
    n: The number of iterations or steps. If no input is given, lim will be used.
    lim: (Stop criteria) - The lower limit for the absolute value of m(xk)
    where xk is the current approximation of the root.
    Default for lim is 0.001.
    Output:
    An approximation of x where m(x) = x
    """
    tab = []
    sol = x0
    count = 0
    spec_tab = [["n", "xn", "|f(xn)|"], [0, x0, abs(m(x0)-x0)]]
    if n == 0:
        while abs(m(sol)-sol) >= lim:
            tab.append([sol, m(sol)])
            sol = m(sol)
            count += 1
            spec_tab.append([count, sol, abs(m(sol))])
    else:
        for k in range(0, n):
            tab.append([sol, m(sol)])
            sol = m(sol)
            spec_tab.append([count, sol, abs(m(sol))])

    return spec_tab


def nr(m, dm, x0, n=0, lim=0.001):
    """
    A function for approximating the root of a function using the Newton-Raphson method
    Input:
    m: The function for which you wish to approximate the root
    dm: The derivative of m
    x0: The initial value
    n: The number of iterations or steps. If no input is given, lim will be used.
    lim: (Stop criteria) - A lower limit for the absolute value of m(xk) where xk is the current approximation
    Default for lim is 0.001.
    Output:
    An approximation for x where m(x) = 0
    """
    tab = []
    sol = x0
    count = 0
    spec_tab = [["n", "xn", "|f(xn)|"], [0, x0, abs(m(x0))]]

    if n == 0:
        while abs(m(sol)) >= lim:
            tab.append([sol, (sol - m(sol)/dm(sol))])
            sol = sol - m(sol)/dm(sol)
            count += 1
            spec_tab.append([count, sol, abs(m(sol))])
    else:
        for k in range(1, n+1):
            tab.append([sol, (sol - m(sol)/dm(sol))])
            sol = sol - m(sol) / dm(sol)
            spec_tab.append([k, sol, abs(m(sol))])

    return spec_tab


def lr(m, a, b, n=100):
    """
    A function for approximating an integral using the Left-hand Rule for rectangles
    Input:
    m: The function to be integrated, as a python function
    a: The lower bound on the integral
    b: The upper bound on the integral
    n: The number of intervals to be used, default is 100
    Output:
    An approximation of the integral
    """
    h = (b-a)/n
    x = [a + i * h for i in range(0, n+1)]
    y = [m(k) for k in x]
    total = 0
    for i in range(0, n):
        total = total + y[i]*h
    return total


def rr(m, a, b, n=100):
    """
    A function for approximating an integral using the Right-hand Rule for rectangles
    Input:
    m: The function to be integrated, as a python function
    a: The lower bound on the integral
    b: The upper bound on the integral
    n: The number of intervals to be used, default is 100
    Output:
    An approximation of the integral
    """
    h = (b - a) / n
    x = [a + i * h for i in range(0, n + 1)]
    y = [m(k) for k in x]
    total = 0
    for i in range(1, n+1):
        total = total + y[i]*h
    return total


def mr(m, a, b, n=100):
    """
    A function for approximating an integral using the Midpoint Rule for rectangles
    Input:
    m: The function to be integrated, as a python function
    a: The lower bound on the integral
    b: The upper bound on the integral
    n: The number of intervals to be used, default is 100
    Output:
    An approximation of the integral
    """
    h = (b - a) / n
    x = [a + i * h for i in range(0, n + 1)]
    x_mid = [(x[i] + x[i+1])/2 for i in range(0, len(x) - 1)]
    y_mid = [m(k) for k in x_mid]
    total = 0
    for i in range(0, n):
        total = total + y_mid[i] * h
    return total


def t(m, a, b, n=100):
    """
    A function for approximating an integral using the Trapezoidal Rule
    Input:
    m: The function to be integrated, as a python function
    a: The lower bound on the integral
    b: The upper bound on the integral
    n: The number of intervals to be used, default is 100
    Output:
    An approximation of the integral
    """
    h = (b - a) / n
    x = [a + i * h for i in range(0, n + 1)]
    y = [m(k) for k in x]
    total = 0
    for i in range(1, n+1):
        total = total + h * 0.5 * (y[i] + y[i-1])
    return total


def s(m, a, b, n=100):
    """
    A function for approximating an integral using Simpson's Rule
    Input:
    m: The function to be integrated, as a python function
    a: The lower bound on the integral
    b: The upper bound on the integral
    n: The number of intervals to be used, default is 100 (n must be even)
    Output:
    An approximation of the integral
    """
    h = (b - a) / n
    x = [a + i * h for i in range(0, n + 1)]
    y = [m(k) for k in x]
    # print(x)
    # print(y)
    if n % 2 == 0:
        m = n//2
        total = 0
        for i in range(1, m+1):
            total = total + (h/3) * (y[2*i - 2] + 4 * y[2*i - 1] + y[2*i])
        return total
    else:
        return "Error: n must be an even number for Simpson's rule"


def e(m, a, b, x0, n=100):
    """
    A function for
    """
    h = (b-a)/n
    sol = x0
    for k in range(0, n):
        sol = sol + h * m(sol)
    return sol
