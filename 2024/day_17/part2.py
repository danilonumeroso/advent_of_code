import re

A, B, C = 0, 1, 2  # Registers
ADV, BXL, BST, JNZ, BXC, OUT, BDV, CDV = 0, 1, 2, 3, 4, 5, 6, 7  # Instructions


def read_file(file_path):
    """
    Register A: 729
    Register B: 0
    Register C: 0

    Program: 0,1,5,4,3,0
    """
    with open(file_path, "r") as file:
        content = file.read()

    parts = content.split("\n\n")

    registers = list(map(int, re.findall(r"\d+", parts[0])))
    program = list(map(int, re.findall(r"\d", parts[1])))

    return registers, program


def combo(operand, registers):
    if 0 <= operand <= 3:
        return operand

    if operand == 4:
        return registers[A]

    if operand == 5:
        return registers[B]

    if operand == 6:
        return registers[C]

    raise ValueError("Invalid operand")


def literal(operand):
    return operand


def main(inp):
    registers, program = inp
    res = []
    pc = 0
    op_used = set()
    while pc < len(program):
        opcode = program[pc]
        operand = program[pc + 1]

        if opcode == ADV:
            # DIV(A, 2^combo(operand)) -> A
            registers[A] = registers[A] >> combo(operand, registers)
            pc += 2
        elif opcode == BXL:
            # XOR(B, literal(operand)) -> B
            registers[B] = registers[B] ^ literal(operand)
            pc += 2
        elif opcode == BST:
            # MOD(combo(operand), 8) -> B
            registers[B] = combo(operand, registers) % 8
            pc += 2
        elif opcode == JNZ:
            # if A == 0: do nothing
            # else: PC = literal(operand)
            if registers[A] != 0:
                pc = literal(operand)
            else:
                pc += 2
        elif opcode == BXC:
            # XOR(B, C) -> B
            registers[B] = registers[B] ^ registers[C]
            pc += 2
        elif opcode == OUT:
            # OUT(MOD(combo(operand), 8)) -> res
            res.append(str(combo(operand, registers) % 8))
            pc += 2
        elif opcode == BDV:
            # DIV(A, 2^combo(operand)) -> B
            registers[B] = registers[A] >> combo(operand, registers)
            pc += 2
        elif opcode == CDV:
            # DIV(A, 2^combo(operand)) -> C
            registers[C] = registers[A] >> combo(operand, registers)
            pc += 2

    return ",".join(res)


def fit_poly(program, a=0):
    if len(program) == 0:
        return a
    for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:  # Possible values of a_i
        a_i = a * 8 + i
        b = a_i % 8
        b = b ^ 3
        c = a_i >> b  # a_i // 2^b
        b = b ^ c
        b = b ^ 5

        if b % 8 == program[-1]:
            res = fit_poly(program[:-1], a_i)
            if res != -1:
                return res

    return -1


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    from tqdm import tqdm

    """
    The program in input.txt is:
    B = A % 8
    B = B XOR 3
    C = A // 2^B
    A = A // 8
    B = B XOR C
    B = B XOR 5
    output B % 8

    we can just reverse engineer the program to get the initial value of A.

    A should be >= 8^15, since we are dividing A by 8 in the program at each iteration
    and we should output at least 16 values (the program terminates when A == 0).

    In other words, we should find the coefficients of the polynomial:
    p(a_0, ..., a_15) = a_0*(8^15) + a_2*(8^14) + ... + a_15*8^0
    such that program(p(a_0, ..., a_15)) = 2,4,1,3,7,5,0,3,4,1,1,5,5,5,3,0
    """

    _, program = inp

    ans = fit_poly(program)
    print("Initial value:", ans)
    inp[0][A] = ans
    result = main(inp)
    print(f"Result:", result)


# 6 * 8**15
#             + 1 * 8**14
#             + 1 * 8**13
#             + 1 * 8**12
#             + 1 * 8**11
#             + 2 * 8**10
#             + 1 * 8**9