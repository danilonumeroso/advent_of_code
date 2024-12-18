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


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
