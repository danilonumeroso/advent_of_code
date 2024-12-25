import numpy as np


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()

    blocks = content.split("\n\n")

    locks, keys = [], []

    for block in blocks:

        if block[0][0] == "#":
            locks.append([-1] * 5)
        else:
            keys.append([6] * 5)

        for line in block.split("\n"):
            for i, char in enumerate(line):
                if block[0][0] == "#" and char == "#":
                    locks[-1][i] += 1
                elif block[0][0] == "." and char == ".":
                    keys[-1][i] -= 1

    return locks, keys


def main(inp):
    res = 0
    locks, keys = np.array(inp[0]), np.array(inp[1])
    for lock in locks:
        for key in keys:
            if np.all(lock + key <= 5):
                res += 1
    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
