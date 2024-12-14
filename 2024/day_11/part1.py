import re

from tqdm import tqdm


def read_file(file_path):
    with open(file_path, "r") as file:
        return list(map(int, file.read().strip().split(" ")))


def blink(stones):
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        elif (stone_len := len(str(stone))) % 2 == 0:
            new_stones.append(int(str(stone)[: stone_len // 2]))
            new_stones.append(int(str(stone)[stone_len // 2 :]))
        else:
            new_stones.append(stone * 2024)

    return new_stones


def main(stones):
    for _ in tqdm(range(25)):
        stones = blink(stones)

    return len(stones)


if __name__ == "__main__":
    file_path = "input.txt"
    stones = read_file(file_path)
    result = main(stones)
    print("Result:", result)
