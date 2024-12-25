from collections import defaultdict


def read_file(file_path):
    with open(file_path, "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def main(secrets):
    total = defaultdict(int)
    for n in secrets:
        seqs = dict()
        change = (0, 0, 0, 0)
        for i in range(2000):
            prev = n % 10
            n = (n ^ (n << 6)) % 16777216
            n = (n ^ (n >> 5)) % 16777216
            n = (n ^ (n << 11)) % 16777216
            change = (*change[1:], n % 10 - prev)
            if i >= 3 and change not in seqs:
                seqs[change] = n % 10
        for s in seqs:
            total[s] += seqs[s]
    res = sorted([(v, k) for k, v in total.items()])[-1][0]
    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
