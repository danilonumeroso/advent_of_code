import re


def read_file(file_path):
    with open(file_path, "r") as file:
        return [l.strip() for l in file.readlines()]


def compute_frequency(l):
    frequencies = {}
    for x in l:
        if x not in frequencies:
            frequencies[x] = 0
        frequencies[x] += 1
    return frequencies


def compute_similarity_score(list_1, list_2):
    frequencies = compute_frequency(list_2)
    similarity_score = 0
    for x1 in list_1:
        if x1 in frequencies:
            similarity_score += x1 * frequencies[x1]

    return similarity_score


def main(input_data):
    # 1. Trasform ["1  2"] -> ([1], [2])
    lists = [list(map(int, re.split(r"\s+", line))) for line in input_data]

    # 2. Split the lists into the two columns
    col_1 = [l[0] for l in lists]
    col_2 = [l[1] for l in lists]

    # 3. Find the total distance
    return compute_similarity_score(col_1, col_2)


if __name__ == "__main__":
    file_path = "input.txt"
    lines = read_file(file_path)

    result = main(lines)
    print("Result:", result)
