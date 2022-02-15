import numexpr as ne
x = float(input("Enter X0: "))
func = input("Enter the function: ")
derivative = input("Enter the function's derivative: ")
approxNum = int(input("n = ?: "))
for i in range(approxNum):
    evalFunc = float(ne.evaluate(func))
    evalDeriv = float(ne.evaluate(derivative))
    x = x - evalFunc / evalDeriv


print(x)

