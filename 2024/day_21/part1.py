NUM_PAD = {
    "N": (0, 0),
    "0": (1, 0),
    "A": (2, 0),
    "1": (0, 1),
    "2": (1, 1),
    "3": (2, 1),
    "4": (0, 2),
    "5": (1, 2),
    "6": (2, 2),
    "7": (0, 3),
    "8": (1, 3),
    "9": (2, 3),
}

ARROW_PAD = {
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0),
    "N": (0, 1),
    "^": (1, 1),
    "A": (2, 1),
}

DIR = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0),
}


def read_file(file_path):
    with open(file_path, "r") as file:
        return [line.strip() for line in file.readlines()]


def l1_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def sub_tuple(a, b):
    return (a[0] - b[0], a[1] - b[1])


def to_arrows(a, arrow_pad=False):
    str = ""

    if a[1] > 0:
        str += "^" * abs(a[1])

    if a[0] < 0:
        str += "<" * abs(a[0])

    if a[0] > 0:
        str += ">" * abs(a[0])

    if a[1] < 0:
        str += "v" * abs(a[1])

    return str + "A"


def to_arrows_2(a, arrow_pad=False):
    str = ""

    if a[1] < 0:
        str += "v" * abs(a[1])

    if a[0] < 0:
        str += "<" * abs(a[0])

    if a[1] > 0:
        str += "^" * abs(a[1])

    if a[0] > 0:
        str += ">" * abs(a[0])

    return str + "A"


def find_path(pad, start, end):
    diff = (end[0] - start[0], end[1] - start[1])
    possible_moves = ""
    possible_moves += ("<" * abs(diff[0]) if diff[0] < 0 else ">") * abs(diff[0])
    possible_moves += ("v" * abs(diff[1]) if diff[1] < 0 else "^") * abs(diff[1])

    def _find(start, end, solution=""):
        if start == end:
            return solution

        if start == pad["N"]:
            return None

        if len(solution) >= len(possible_moves):
            return None

        for move in possible_moves:
            new_pos = (start[0] + DIR[move][0], start[1] + DIR[move][1])
            if sol := _find(new_pos, end, solution=solution + move):
                return sol

        return None

    return _find(start, end) + "A"


def main(codes):
    res = 0

    # Robots: A, B, C

    pos_a, pos_b, pos_c = "A", "A", "A"
    for code_a in codes:
        count = 0
        steps_str = ""
        for c_a in code_a:
            # Move robot A
            start_a, end_a = NUM_PAD[pos_a], NUM_PAD[c_a]
            mov_a = sub_tuple(end_a, start_a)
            code_b = to_arrows(mov_a)
            # code_b = find_path(NUM_PAD, NUM_PAD[pos_a], NUM_PAD[c_a])
            pos_a = c_a
            # print(code_b_leg)
            for c_b in code_b:
                # Move robot B
                start_b, end_b = ARROW_PAD[pos_b], ARROW_PAD[c_b]
                mov_b = sub_tuple(end_b, start_b)
                code_c = to_arrows(mov_b)
                # code_c = find_path(ARROW_PAD, ARROW_PAD[pos_b], ARROW_PAD[c_b])
                # print(code_c)
                # print(code_c_leg)
                pos_b = c_b
                # print(code_c)
                # steps_str += code_c
                for c_c in code_c:
                    # Move robot C and count steps
                    start_c, end_c = ARROW_PAD[pos_c], ARROW_PAD[c_c]
                    mov_c = sub_tuple(end_c, start_c)
                    code_d = to_arrows(mov_c)
                    # code_d = find_path(ARROW_PAD, ARROW_PAD[pos_c], ARROW_PAD[c_c])
                    steps_str += code_d
                    # print(c_c, code_d)
                    count += l1_distance(ARROW_PAD[pos_c], ARROW_PAD[c_c]) + 1
                    pos_c = c_c
            # print("-------------------")
        # print(steps_str, len(steps_str))
        print(f"{count} * {code_a[:3]}")
        res += count * int(code_a[:3])
    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
