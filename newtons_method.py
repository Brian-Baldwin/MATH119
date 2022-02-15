import numexpr as ne


def newtons_method(x, func, derivative):
    approxNum = int(input("n = ?: "))
    for i in range(approxNum):
        evalFunc = float(ne.evaluate(func))
        evalDeriv = float(ne.evaluate(derivative))
        x = x - evalFunc / evalDeriv
    return x


if __name__ == "__main__":
    a = float(input("Enter X0: "))
    funct = input("Enter the function: ")
    der = str(input("Enter the function's derivative: "))
    print(newtons_method(a, funct, der))
