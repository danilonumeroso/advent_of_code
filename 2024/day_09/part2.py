import re


def read_file(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()

    memory = []
    for i in range(len(content)):
        if i % 2 == 0:
            memory.append((i // 2, int(content[i])))
        else:
            memory.append(("s", int(content[i])))

    return memory


def can_be_moved_left(block_id, block_size, spaces):
    for s in [s for s in spaces.keys() if s < block_id]:
        if spaces[s] >= block_size:
            return True
    return False


def compact_contiguous_spaces_inplace(memory, i):
    j = i + 1
    while j < len(memory) and memory[j][0] == "s":
        memory[i] = ("s", memory[i][1] + memory[j][1])
        memory.pop(j)

    j = i - 1

    while j >= 0 and memory[j][0] == "s":
        memory[i] = ("s", memory[i][1] + memory[j][1])
        memory.pop(j)


def allocate(memory):
    for i in range(len(memory) - 1, -1, -1):
        cell = memory[i]
        if cell[0] == "s":
            continue

        block_id, block_size = cell
        for j, cell2 in enumerate(memory):
            if j >= i:
                break
            # Remove from memory element of index i
            if cell2[0] != "s":
                continue

            _, size = cell2

            if size >= block_size:
                memory[i] = ("s", block_size)
                # compact_contiguous_spaces_inplace(memory, i)

                if size - block_size > 0:
                    memory[j] = ("s", size - block_size)
                    memory.insert(j, cell)
                else:
                    memory[j] = cell
                break

    return memory


def main(memory):
    res = 0
    allocations = allocate(memory)
    start = 0
    for block_id, length in allocations:
        for _ in range(length):
            # print(f"start * block = {start} * {block_id} = {start * block_id}")
            if block_id != "s":
                res += start * block_id
            start += 1

    return res


if __name__ == "__main__":
    file_path = "input.txt"
    memory = read_file(file_path)
    result = main(memory)
    print("Result:", result)
