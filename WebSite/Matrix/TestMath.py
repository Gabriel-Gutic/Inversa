from sympy import *


def TestMath() -> str:
    M = Matrix([[10, "((2 + 3j) * x^2 + 2) / y"], ["x-10", 4]])

    s: str = str(M.det())
    s = s.replace("**", "^")
    s = s.replace("*", "∙")
    return s
