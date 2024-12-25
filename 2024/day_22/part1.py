def read_file(file_path):
    with open(file_path, "r") as file:
        return [int(line.strip()) for line in file.readlines()]


def evolve(secret):
    """In particular, each buyer's secret number evolves into the next secret number in the sequence via the following process:

    Calculate the result of multiplying the secret number by 64. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of dividing the secret number by 32. Round the result down to the nearest integer. Then, mix this result into the secret number. Finally, prune the secret number.
    Calculate the result of multiplying the secret number by 2048. Then, mix this result into the secret number. Finally, prune the secret number.
    Each step of the above process involves mixing and pruning:

    To mix a value into the secret number, calculate the bitwise XOR of the given value and the secret number. Then, the secret number becomes the result of that operation. (If the secret number is 42 and you were to mix 15 into the secret number, the secret number would become 37.)
    To prune the secret number, calculate the value of the secret number modulo 16777216. Then, the secret number becomes the result of that operation. (If the secret number is 100000000 and you were to prune the secret number, the secret number would become 16113920.)
    """

    for _ in range(2000):
        secret = (secret << 6) ^ secret
        secret %= 16_777_216

        secret = (secret >> 5) ^ secret
        secret %= 16_777_216

        secret = (secret << 11) ^ secret
        secret %= 16_777_216

    return secret


def main(secrets):
    res = 0

    for secret in secrets:
        res += evolve(secret)
    return res


if __name__ == "__main__":
    file_path = "input.txt"
    inp = read_file(file_path)
    result = main(inp)
    print("Result:", result)
