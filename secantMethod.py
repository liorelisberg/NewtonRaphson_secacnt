def secant_method(f, x0, x1, epsilon):
    x2 = 0
    step = 1
    tol = True

    while tol:
        if f(x0) == f(x1):
            print("Divide by zero")
            break

        x2 = x0 - (x1 - x0) * f(x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        step += 1

        tol = abs(f(x2)) > epsilon
    return x2
