import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def multiply_and_sum(lists):
    res = 0
    for l in lists:
        res += sum(x * y for x, y in l)
    return res


def find_instructions(input_data):
    # Find all mul(X, Y), do() and don't().
    instructions = []

    for line in input_data:
        muls = [
            (match.start(), match.end())
            for match in re.finditer(r"mul\(\d+,\d+\)", line)
        ]
        dos = [(match.start(), match.end()) for match in re.finditer(r"do\(\)", line)]

        donts = [
            (match.start(), match.end()) for match in re.finditer(r"don't\(\)", line)
        ]

        instructions.append(muls + dos + donts)

    return instructions


def sort_and_textify_instructions(programs, source_code):
    for i in range(len(programs)):
        programs[i] = sorted(programs[i], key=lambda x: x[0])
        programs[i] = [source_code[i][p[0] : p[1]] for p in programs[i]]

    return programs


def execute(program):
    # Execute the program
    enable_mul = True
    res = 0

    for instruction in program:
        if instruction.startswith("mul"):
            if not enable_mul:
                continue

            factors = re.findall(r"\d+", instruction)
            assert len(factors) == 2
            res += int(factors[0]) * int(factors[1])
        elif instruction == "do()":
            enable_mul = True
        elif instruction == "don't()":
            enable_mul = False
        else:
            raise ValueError(f"Unknown instruction: {instruction}")

    return res


def main(input_data):
    subprograms = find_instructions(input_data)
    subprograms = sort_and_textify_instructions(subprograms, input_data)

    # Multiple
    program = []
    for p in subprograms:
        program.extend(p)

    return execute(program)


if __name__ == "__main__":
    file_path = "input.txt"
    lines = read_file(file_path)

    result = main(lines)
    print("Result:", result)
