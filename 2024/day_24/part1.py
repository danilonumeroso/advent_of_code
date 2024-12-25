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
    while len(instructions) > len(done):
        op, x1, x2, y = instructions[i]

        if op == "AND":
            if (x1 in gates and not gates[x1]) or (x2 in gates and not gates[x2]):
                gates[y] = 0
                done.add(i)
            elif x1 in gates and x2 in gates:
                gates[y] = gates[x1] & gates[x2]
                done.add(i)
        elif op == "OR":
            if (x1 in gates and gates[x1]) or (x2 in gates and gates[x2]):
                gates[y] = 1
                done.add(i)
            elif x1 in gates and x2 in gates:
                gates[y] = gates[x1] | gates[x2]
                done.add(i)
        elif op == "XOR":
            if x1 in gates and x2 in gates:
                gates[y] = gates[x1] ^ gates[x2]
                done.add(i)

        i = (i + 1) % len(instructions)

    z_gates = sorted([(x, gates[x]) for x in gates if x.startswith("z")], reverse=True)
    return int("".join([str(x[1]) for x in z_gates]), base=2)


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
