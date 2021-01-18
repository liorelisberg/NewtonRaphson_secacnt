from scipy import misc


def newton_method(f, x0, x1, eps):
    step = 0
    x2 = x0

    while True:
        fxn = f(x2)
        if abs(fxn) < eps:
            print(f"range: [{x0} ,{x1}]: in {step} iterations: {x2}")
            break
        f_derivative = misc.derivative(f, x2)
        if f_derivative == 0:
            print("No solution found.")
            break
        x2 = x2 - fxn / f_derivative
        step += 1

    return x2
