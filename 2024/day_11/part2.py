import re
from functools import cache


def read_file(file_path):
    with open(file_path, "r") as file:
        return list(map(int, file.read().strip().split(" ")))


@cache
def blink(stone, steps):
    if steps == 0:
        return 1

    if stone == 0:
        return blink(1, steps - 1)

    if (stone_len := len(str(stone))) % 2 == 0:
        return blink(int(str(stone)[: stone_len // 2]), steps - 1) + blink(
            int(str(stone)[stone_len // 2 :]), steps - 1
        )

    return blink(stone * 2024, steps - 1)


def main(stones):
    return sum(blink(s, 75) for s in stones)


if __name__ == "__main__":
    file_path = "input.txt"
    stones = read_file(file_path)
    result = main(stones)
    print("Result:", result)
