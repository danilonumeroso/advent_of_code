import re


def read_file(file_path):

    def to_dict(rules):
        d = {}

        for r in rules.split("\n"):
            k, v = r.split("|")
            k, v = int(k), int(v)

            if k not in d:
                d[k] = []

            d[k].append(v)

        return d

    with open(file_path, "r") as file:
        content = file.read()

    rules, updates = content.split("\n\n")

    return to_dict(rules), [list(map(int, u.split(","))) for u in updates.split("\n")]


def is_in_right_order(update, rules):
    """
    Check if the update is in the right order.
    The update is in the right order if it does not violate any precedence rule.
    E.g. if rules = {a: [b]}, then u = [b, a] is not in the right order since 'a' must come before 'b'.
    """
    for i, u1 in enumerate(update):
        rest = update[i + 1 :]

        for u2 in rest:
            if u2 not in rules:
                continue

            if u1 in rules[u2]:
                return False
    return True


def sort_update(update, rules):
    """
    Implement a standard selection sort to sort the updates that violate the ordering rules.
    """
    n = len(update)

    for i in range(n):
        idx = i

        for j in range(i + 1, n):
            if update[j] not in rules or update[j] in rules.get(update[idx], []):
                continue

            if update[i] in rules[update[j]]:
                idx = j
                update[i], update[idx] = update[idx], update[i]

    return update


def main(rules, updates):
    wrong_updates = [u for u in updates if not is_in_right_order(u, rules)]
    corrected_updates = list(map(lambda u: sort_update(u, rules), wrong_updates))
    return sum(map(lambda u: u[len(u) // 2], corrected_updates))


if __name__ == "__main__":
    file_path = "input.txt"
    rules, updates = read_file(file_path)
    result = main(rules, updates)
    print("Result:", result)
