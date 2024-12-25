import re
from collections import defaultdict


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    init_txt, instructions_txt = content.split("\n\n")

    gates = {
        re.findall(r"\w+", line)[0]: int(line.split(":")[1].strip())
        for line in init_txt.split("\n")
    }
    instructions = []

    for line in instructions_txt.split("\n"):
        instr = re.findall(r"\w+", line)
        instructions.append((instr[1], instr[0], instr[2], instr[3]))

    return gates, instructions


def main(inp):
    gates, instructions = inp
    done = set()
    i = 0
    wrong_gates = set()
    highest_z = "z45"
    for op, x1, x2, y in instructions:
        if y[0] == "z" and op != "XOR" and y != highest_z:
            wrong_gates.add(y)
        if (
            op == "XOR"
            and y[0] not in ["x", "y", "z"]
            and x1[0] not in ["x", "y", "z"]
            and x2[0] not in ["x", "y", "z"]
        ):
            wrong_gates.add(y)
        if op == "AND" and "x00" not in [x1, x2]:
            for sub_op, sub_x1, sub_x2, sub_y in instructions:
                if (y == sub_x1 or y == sub_x2) and sub_op != "OR":
                    wrong_gates.add(y)
        if op == "XOR":
            for sub_op, sub_x1, sub_x2, sub_y in instructions:
                if (y == sub_x1 or y == sub_x2) and sub_op == "OR":
                    wrong_gates.add(y)

    return ",".join(sorted(wrong_gates))


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
