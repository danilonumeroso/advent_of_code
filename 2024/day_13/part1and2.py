import re

from sympy import Eq, linsolve, symbols

BIG_NUMBER = 10000000000000  # set to 0 for part 1


def read_file(file_path):
    """Button A: X+94, Y+34
    Button B: X+22, Y+67
    Prize: X=8400, Y=5400

    Button A: X+26, Y+66
    Button B: X+67, Y+21
    Prize: X=12748, Y=12176

    Button A: X+17, Y+86
    Button B: X+84, Y+37
    Prize: X=7870, Y=6450

    Button A: X+69, Y+23
    Button B: X+27, Y+71
    Prize: X=18641, Y=10279"""
    with open(file_path, "r") as file:
        content = file.read().split("\n\n")

    As = []
    Bs = []
    prize = []
    for part in content:
        a, b, p = part.split("\n")
        As.append(list(map(int, re.findall(r"\d+", a))))
        Bs.append(list(map(int, re.findall(r"\d+", b))))
        prize.append(
            list(map(lambda x: x + BIG_NUMBER, map(int, re.findall(r"\d+", p))))
        )

    return As, Bs, prize


def main(input):
    As, Bs, prize = input
    res = 0

    """
       Diophantine equations!
       Button A: X+94, Y+34
       Button B: X+22, Y+67
       Prize: X=8400, Y=5400
       
       --> [94 34 ; 22 67] * [a ; b] = [8400 ; 5400]

       solve for a and b where a and b are integers.
       Since I'm too lazy to implement the solver by hand, I'll use sympy's linsolve.
       """

    for coeff_a, coeff_b, p in zip(As, Bs, prize):
        var_a, var_b = symbols("a b", integer=True)
        eq1 = Eq(var_a * coeff_a[0] + var_b * coeff_b[0], p[0])
        eq2 = Eq(var_a * coeff_a[1] + var_b * coeff_b[1], p[1])
        sol = linsolve([eq1, eq2], var_a, var_b)
        a_, b_ = sol.args[0][0], sol.args[0][1]

        if str.isdigit(str(a_)) and str.isdigit(
            str(b_)
        ):  # Check if the solutions are integers
            res += a_ * 3 + b_

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
